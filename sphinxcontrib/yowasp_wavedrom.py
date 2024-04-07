import re
import json
from pathlib import Path, PosixPath
from docutils.parsers.rst import Directive
from docutils import nodes
import sphinx.application
import sphinx.writers.html5
import yowasp_wavedrom


class WaveDromDirective(Directive):
    required_arguments = 1
    has_content = True

    def run(self):
        self.assert_has_content()

        # Extract basename of the generated image file.
        name, = self.arguments

        # This is a really weird way to extract the payload of a directive, but it keeps accurate
        # line and more importantly column numbers within `JSONDecodeError`.
        payload = re.sub(r"^..\s+wavedrom\s*::.+?\n", "\n", self.block_text)

        # Parse and validate WaveJSON source.
        try:
            wavedrom_src = json.loads(payload)
        except json.decoder.JSONDecodeError as error:
            return [self.reporter.error(
                f"line {error.lineno + self.lineno - 1}, column {error.colno}: "
                f"JSON: {error.msg}"
            )]

        node = wavedrom_diagram(self.block_text, name=name, src=wavedrom_src,
            loc=f'{self.state.document["source"]}:{self.lineno}')
        self.add_name(node)
        return [node]


class wavedrom_diagram(nodes.General, nodes.Inline, nodes.Element):
    pass


def html_visit_wavedrom_diagram(self: sphinx.writers.html5.HTML5Translator, node: wavedrom_diagram):
    basename: str = node["name"]
    wavedrom_loc: str = node["loc"]
    wavedrom_src: dict = node["src"]

    # Adjust diagram configuration according to builder configuration.
    wavedrom_src_config = wavedrom_src.setdefault("config", {})
    if "signal" in wavedrom_src:
        wavedrom_src_config.setdefault("skin", self.builder.config.yowasp_wavedrom_skin)

    # Render WaveJSON to an SVG.
    try:
        wavedrom_svg = yowasp_wavedrom.render(wavedrom_src)
    except Exception as error:
        sphinx.application.logger.error(
            f'Could not render WaveDrom diagram at {wavedrom_loc}: {error}')
        self.body.append(f'<em style="color:red;font-weight:bold">'
            f'<pre>/!\ Could not render WaveDrom diagram: {self.encode(error)}</pre>'
            f'</em>')
        raise nodes.SkipNode
    
    # Write the SVG to output directory. This is necessary because inlining it into the HTML has
    # significantly different behavior: duplicate IDs result in broken rendering, text can be
    # selected, media queries can't be overridden with a `color-scheme` CSS attribute for themes
    # that have a dark/light toggle via JS, etc.
    pathname = Path(self.builder.outdir).joinpath(
        # Note that for documents in subdirectories, the image directory is placed within that
        # subdirectory. The other option would be to use enough `../` to locate the top-level
        # image directory; using leading `/` in the `<img>` tag isn't feasible since that would
        # break on `file:///` URLs.
        PosixPath(self.builder.current_docname).parent,
        self.builder.imagedir,
        f'{basename}.svg'
    )
    pathname.parent.mkdir(parents=True, exist_ok=True)
    pathname.write_text(wavedrom_svg)

    # Reference the SVG in the HTML document.
    self.body.append(f'<img src="{self.builder.imagedir}/{basename}.svg" '
        f'alt="{self.encode(node["src"])}">')
    raise nodes.SkipNode


def setup(app: sphinx.application.Sphinx):
    app.add_config_value("yowasp_wavedrom_skin", "default", "html", str)
    app.add_directive("wavedrom", WaveDromDirective)
    app.add_node(wavedrom_diagram,
        html=(html_visit_wavedrom_diagram, None))
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }
