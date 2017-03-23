stuff2str
=========
Python tool for embedding file contents in JavaScript as strings.
Usefull for making Greasemonkey scripts when we want to use variables
containing inline CSS or HTML in our script.

Installation
------------
Use pip my dude.

::

    pip3 install https://github.com/Szero/stuff2str/archive/master.zip


Windows user might wanna try, after installing python3 that is:

::

    py -3 -m pip install https://github.com/Szero/stuff2str/archive/master.zip

Usage
-----
Firstly, insert :code:`str2string("/path/to/file")` variable into your JavaScript file.

After that, use one of the commands listed below:

::

    stuff2str INFILE OUTFILE
    stuff2str -o INFILE
    stuff2str --help



Windows user might wanna try:

::

    py -3 -m stuff2str ...

If our referenced file is looking like this ...

::

    this is
    my swamp

... than, the variable will get expanded to something looking like this:

::
    ["this is",
    "my swamp"
    ].join("\n")
