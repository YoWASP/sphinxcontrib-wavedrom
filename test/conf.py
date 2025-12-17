project = "WaveDrom extension for Sphinx"
extensions = ["sphinxcontrib.yowasp_wavedrom"]
master_doc = "index"

# Use furo theme if available (not compatible with Sphinx 9 yet), otherwise alabaster
try:
    import furo
    html_theme = "furo"
except ImportError:
    html_theme = "alabaster"

html_static_path = ["_static"]
html_css_files = ["wavedrom.css"]
html_extra_path = [".nojekyll"]

# yowasp_wavedrom_skin = "default"
