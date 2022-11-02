#!/usr/bin/python3
"""this module contains a script to display a header variable from a url"""

if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as req:
        print(req.info()['x-Request-Id'])
