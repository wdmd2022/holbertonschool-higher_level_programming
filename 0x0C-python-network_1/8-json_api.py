#!/usr/bin/python3
"""this script takes in a letter and sends a POST request to the local server
(http://0.0.0.0:5000/search_user with the letter as a parameter (variable 'q')
If no letter is given, it sets q="" and if the reponse body is properly JSON
formatted (and not empty), it displays the id and name like this:
[<id>] <name>... otherwise, it displays "Not a valid JSON" if the JSON is
invalid, or "No result" if the JSON is empty."""

if __name__ == "__main__":
    import requests
    from sys import argv
    qvalue = ""
    if len(argv) > 1:
        qvalue = argv[1]
    qload = {'q': qvalue}
    r = requests.post('http://0.0.0.0:5000/search_user', data=qload)
    try:
        jayzin = r.json()
        if len(jayzin) == 0:
            print("No result")
        else:
            print("[{}] {}".format(jayzin.get('id'), jayzin.get('name')))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
