#!/usr/bin/env python3
"""Setting it all up like a real human bean"""

import re
from setuptools import setup


def version(filename):
    """Thanks python!"""
    with open(filename) as filep:
        return re.search('__version__ = "(.+?)"', filep.read()).group(1)


setup(
    name="stuff2str",
    version=version("stuff2str/_version.py"),
    description="Convert files into JavaScript-embeddable strings",
    long_description=open("README.rst").read(),
    url="https://github.com/Szero/stuff2str",
    license="MIT",
    author="Szero",
    author_email="singleton@tfwno.gf",
    entry_points={"console_scripts": ["stuff2str = stuff2str.__main__:run"]},
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities :: Build_Systems",
        "Topic :: JavaScript"
    ],
    install_requires=["path.py>=10.0"])
