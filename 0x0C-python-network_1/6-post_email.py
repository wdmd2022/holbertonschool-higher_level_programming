#!/usr/bin/python3
"""this script takes in a URL and an email address, then sends a POST
reqest to that URL with the email as a parameter, and finally displays
the body of the response"""

if __name__ == "__main__":
    import requests
    from sys import argv

    emaildata = {'email': argv[2]}
    r = requests.post(argv[1], data=emaildata)
    print(r.text)
