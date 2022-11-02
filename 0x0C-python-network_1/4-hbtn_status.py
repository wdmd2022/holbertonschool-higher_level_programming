#!/usr/bin/python3
"""fetch the status of the hbtn intranet again, but use requests"""

if __name__ == "__main__":
    from requests import get
    request = get("https://intranet.hbtn.io/status")
    whatgot = request.text
    print("Body response:")
    print("\t- type: {}".format(type(whatgot)))
    print("\t- content: {}".format(whatgot))
