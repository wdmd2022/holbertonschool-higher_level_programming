#!/usr/bin/python3
"""this module contains a script to fetch a url"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as req:
        payoff = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(payoff)))
        print("\t- content: {}".format(payoff))
        print("\t- utf8 content: {}".format(payoff.decode('utf-8')))
