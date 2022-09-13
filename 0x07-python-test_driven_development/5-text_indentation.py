#!/usr/bin/python3
"""this module contains a function that formats a long string
"""

def text_indentation(text):
    """this function formats a long string w/ newlines at '.' ':' or '?'

    Args:
        text (str): the string to be formatted

    Raises:
        TypeError: if text is not a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    flag = 0
    for character in text:
        if flag != 1:
            if character == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if character == "." or character == "?" or character == ":":
                print("{}{}".format(character, "\n"))    
                flag = 0
            else:
                print("{}".format(character), end="")
