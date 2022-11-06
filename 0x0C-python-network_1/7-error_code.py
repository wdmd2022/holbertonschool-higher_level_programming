#!/usr/bin/python3
"""this script takes in a URL, sends a request to it, and displays the
body of the response. If HTTP status code is >= 400, it prints 'Error
code: ' followed by the value of the HTTP status code."""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
