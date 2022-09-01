#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return
    stringtoreturn = ""
    for i in range(len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        stringtoreturn = stringtoreturn + my_string[i]
    return stringtoreturn
