sphinxcontrib-yowasp-wavedrom
=============================

This [Sphinx] extension allows embedding [WaveDrom] waveform, bitfield, and circuit diagrams into Sphinx documents.

This extension uses the [YoWASP WaveDrom][yowasp-wavedrom] package to ensure that diagrams are rendered exactly the same as in the WaveDrom editor, without having to follow a decision tree for configuration, without requiring any additional tools to be installed on the system used to build documentation, without requiring any native dependencies to be installed on that system, without requiring JavaScript for browsing documentation, and without slowing down the Sphinx build process. It also reports syntax and semantic errors with accurate source locations. <!-- environmental storytelling paragraph --> 

WaveJSON diagram descriptions are always converted into SVG files; only the HTML builder is supported at the moment. **Make sure to follow the instructions in the [color schemes] section!**

[Sphinx]: https://www.sphinx-doc.org/
[WaveDrom]: https://wavedrom.com/
[yowasp-wavedrom]: https://github.com/YoWASP/wavedrom
[Furo]: https://github.com/pradyunsg/furo


Usage
-----

This extension provides only one directive, `wavedrom`. Its argument is the base name, without extension, of the generated image file (in `<output directory>/<document directory>/_images/`; which must be unique for that document directory), and its contents is the raw WaveJSON file that can be copied to or from the editor. For example:

```rst
.. wavedrom:: clk_and_data
    
    {"signal": [  
        {"name": "clk",  "wave": "n..."},
        {"name": "data", "wave": "01.0"}
    ]}
```

Additional examples are available [in the test suite](/test/index.rst), as well as the corresponding [rendered output](https://yowasp.github.io/sphinxcontrib-wavedrom/).


Color schemes
-------------
[color schemes]: #color-schemes

By default, the diagrams are responsive to the preferred color scheme as provided by the user agent. This is usually not quite the desired behavior, and can make diagrams unreadable unless the extension is integrated with the chosen Sphinx theme.

For Sphinx themes that only have a light variant, e.g. the [Read the Docs](https://pypi.org/project/sphinx-rtd-theme/) theme, the following [custom CSS](https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html) should be used:

```css
img.wavedrom { color-scheme: light; }
```

For Sphinx themes that have a light variant and a dark variant and a button that switches between them, e.g. the [Furo](https://github.com/pradyunsg/furo) theme, the following custom CSS may be used as a starting point:

```css
:root[data-theme="light"] { img.wavedrom { color-scheme: light; } }
:root[data-theme="dark"] { img.wavedrom { color-scheme: dark; } }
```

It may have to be adjusted to accommodate the particular mechanism the theme is using to keep track of the dynamically selected color scheme preference.

For Sphinx themes that have a light variant and a dark variant and do not have a button to switch between them (i.e. the user agent preference is always followed), the default behavior is sufficient.


Configuration
-------------

The extension recognizes these configuration variables in `conf.py`:

```py
# Default skin for waveforms. If `json["config"]["skin"]` is not set in the directive,
# it defaults to the value of this variable. Does not affect bit fields or circuits.
yowasp_wavedrom_skin = "default"
```


License
-------

This project is distributed under the terms of the [MIT license](LICENSE.txt).
