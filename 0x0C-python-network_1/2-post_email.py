#!/usr/bin/python3
"""this module contains a script to execute a post request using a url
and an email"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("utf-8")
    rekky = urllib.request.Request(url, data)
    with urllib.request.urlopen(rekky) as req:
        print(req.read().decode("utf-8"))
