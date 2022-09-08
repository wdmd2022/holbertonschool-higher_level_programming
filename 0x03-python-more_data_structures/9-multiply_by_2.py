#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    newdict = a_dictionary.copy()
    for k, v in newdict.items():
        newdict[k] = v * 2
    return newdict
