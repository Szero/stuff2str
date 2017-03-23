#!/usr/bin/env python3
"""Setting it all up like a real human bean"""

from setuptools import setup

import re

def version():
    """Thanks python!"""
    with open("stuff2str/_version.py") as filep:
        return re.search('__version__ = "(.+?)"', filep.read()).group(1)


setup(
    name="stuff2str",
    version=version(),
    description="Convert files into JavaScript-embeddable strings",
    long_description=open("README.rst").read(),
    url="https://github.com/Szero/stuff2str",
    license="MIT",
    author="Szero",
    author_email="singleton@tfwno.gf",
    packages=['stuff2str'],
    entry_points={"console_scripts": ["stuff2str = stuff2str.__main__:run"]},
    classifiers=[
        "Development Status :: 0.1 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities :: Build_Systems",
        "Topic :: JavaScript"
    ],
    install_requires=["path.py>=10.0"]
    )
