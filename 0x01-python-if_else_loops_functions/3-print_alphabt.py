#!/usr/bin/python3
for x in range(97, 123):
    if x != ord("q") and x != ord("e"):
        print("{:c}".format(x), end="")
