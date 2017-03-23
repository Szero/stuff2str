#!/usr/bin/env python3

"""Szero's tool for turning files into JavaScript embeddably string."""

import sys

from stuff2str import main

def run():
    """ Run as CLI command """

    sys.exit(main())

if __name__ == "__main__":
    run()
