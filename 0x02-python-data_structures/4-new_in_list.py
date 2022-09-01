#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return
    newlist = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return newlist
    newlist[idx] = element
    return newlist
