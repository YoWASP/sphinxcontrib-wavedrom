Subdirectory example
--------------------

..
    Name intentionally conflicts with the one from a level above.

.. wavedrom:: skin_default

    {
        "signal": [
            {"name": "clk",
             "wave": "0P............"},
            {"name": "rd_port.addr",
             "wave": "==============",
             "data": [0,1,2,3,4,5,6,7,8,9,10,11,0,1],
             "node": ".a"},
            {"name": "rd_port.data",
             "wave": "==============",
             "data": ["H","e","l","l","o"," ","w","o","r","l","d","\\n","H","e"],
             "node": ".d"}
        ],
        "edge": [
            "a-|d"
        ]
    }
