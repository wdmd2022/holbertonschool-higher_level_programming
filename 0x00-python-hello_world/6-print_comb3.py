#!/usr/bin/python3
for x in range(0, 9):
    for y in range(x + 1, 10):
        print("{}{}{}".format(x, y, ", " if x < 8 else "\n"), end="")
