sphinxcontrib-yowasp-wavedrom test page
=======================================


Waveform diagrams
-----------------

default:

.. wavedrom:: skin_default

    {"signal": [
        {"name": "clk",  "wave": "n..."},
        {"name": "data", "wave": "01.0"}
    ]}

.. test trailing commas

light:

.. wavedrom:: skin_light

    {
        "signal": [
            {"name": "clk",  "wave": "p..."},
            {"name": "data", "wave": "01.0"},
        ],
        "config": {"skin": "light"},
    }

.. test ECMAScript object keys
.. test single quoted strings
.. test comments

dark:

.. wavedrom:: skin_dark

    {
        signal: [
            {name: 'clk',  wave: 'p...'},
            // one pulse
            {name: 'data', wave: '01.0'}
        ],
        config: {skin: 'dark'}
    }

narrow:

..
    test nested base names

.. wavedrom:: extra/skin_narrow

    {
        "signal": [
            {"name": "clk",  "wave": "n..."},
            {"name": "data", "wave": "01.0"}
        ],
        "config": {"skin": "narrow"}
    }


Bit field diagrams
------------------

.. wavedrom:: uart_rx_status

    {
        "reg": [
            { "name": "ready",    "bits": 1, "attr": "R" },
            { "name": "overflow", "bits": 1, "attr": "RW1C" },
            { "name": "error",    "bits": 1, "attr": "RW1C" },
            { "bits": 5, "attr": "ResR0W0" }
        ]
    }


Circuit diagrams
----------------

.. wavedrom:: circuit

    {
        "assign": [
            ["out",
                ["|",
                    ["&", ["~", "a"], "b"],
                    ["&", ["~", "b"], "a"]
                ]
            ]
        ]
    }

Subdocument
-----------

.. toctree::

    subdir/index
