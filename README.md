sphinxcontrib-yowasp-wavedrom
=============================

This [Sphinx] extension allows embedding [WaveDrom] waveform, bitfield, and circuit diagrams into Sphinx documents.

This extension uses the [YoWASP WaveDrom][yowasp-wavedrom] package to ensure that diagrams are rendered exactly the same as in the WaveDrom editor, without having to follow a decision tree for configuration, without requiring any additional tools to be installed on the system used to build documentation, without requiring any native dependencies to be installed on that system, without requiring JavaScript for browsing documentation, and without slowing down the Sphinx build process. It also reports syntax and semantic errors with accurate source locations. <!-- environmental storytelling paragraph --> 

WaveJSON diagram descriptions are always converted into SVG files; only the HTML builder is supported at the moment. Sphinx themes with color schemes toggles, like [Furo], are supported by default, but may require [custom CSS](/test/_static/wavedrom.css) for integration.

[Sphinx]: https://www.sphinx-doc.org/
[WaveDrom]: https://wavedrom.com/
[yowasp-wavedrom]: https://github.com/YoWASP/wavedrom
[Furo]: https://github.com/pradyunsg/furo


Usage
-----

This extension provides only one directive, `wavedrom`. Its argument is the base name, without extension, of the generated image file (in `<output directory>/_images/`; which must be unique in the entire document tree), and its contents is the raw WaveJSON file that can be copied to or from the editor. For example:

```rst
.. wavedrom:: clk_and_data
    
    {"signal": [  
        {"name": "clk",  "wave": "n..."},
        {"name": "data", "wave": "01.0"}
    ]}
```

Additional examples are available [in the test suite](/test/index.rst), as well as the corresponding [rendered output](https://yowasp.github.io/sphinxcontrib-wavedrom/).


License
-------

This project is distributed under the terms of the [MIT license](LICENSE.txt).
