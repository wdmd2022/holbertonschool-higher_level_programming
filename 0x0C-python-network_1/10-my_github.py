#!/usr/bin/python3
"""this script takes your GitHub credentials (username, personal access token
as password) and uses the GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get('https://api.github.com/user',
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    uid = r.json()
    print(uid.get('id'))
