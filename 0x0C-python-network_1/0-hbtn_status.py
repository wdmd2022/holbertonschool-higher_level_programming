#!/usr/bin/python3
"""this module contains a script to fetch a url"""

import urllib.request

if __name__ == "__ main __":
    with urllib.request.urlopen(
        urllib.request.Request("https://intranet.hbtn.io/status")) as req:
            payoff = req.read()
            print("Body response:")
            print("\t- type: {}".format(type(payoff)))
            print("\t- content: {}".format(payoff))
            print("\t- utf8 content: {}".format(payoff.decode('utf8')))
