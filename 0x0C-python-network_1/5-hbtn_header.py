#!/usr/bin/python3
"""this script sends a request to the URL provided and displays the
value of variable 'X-Request-Id' in the response header"""

if __name__ == "__main__":
    from sys import argv
    import requests

    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
