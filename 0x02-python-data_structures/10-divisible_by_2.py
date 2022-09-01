#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    newlist = []
    for item in my_list:
        if item % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist
