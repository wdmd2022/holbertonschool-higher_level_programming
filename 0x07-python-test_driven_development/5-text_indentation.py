#!/usr/bin/python3
"""this module contains a function that formats a long string
"""

def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    flag = 0
    for character in text:
        print("{}".format(character), end="")
        if flag == 1:
            print("\n" + "\n")
            flag = 0
        if character == "." or "?" or ":":
            flag = 1
