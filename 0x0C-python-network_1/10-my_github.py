#!/usr/bin/python3
"""this script takes your GitHub credentials (username, personal access token
as password) and uses the GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    logmein = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get('https://api.github.com/user', auth=logmein)
    uid = r.json()
    print(uid.get('id'))
