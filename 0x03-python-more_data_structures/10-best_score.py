#!/usr/bin/python3


def best_score(a_dictionary):
    tempscore = 0
    tempwinner = None
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v >= tempscore:
                tempscore = v
                tempwinner = k
    return tempwinner
