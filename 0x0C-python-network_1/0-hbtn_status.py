#!/usr/bin/python3
"""this module contains a script to fetch a url"""

import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    stuff_we_got = response.read()
    for line in stuff_we_got:
        print("\t- {}".format(line))

