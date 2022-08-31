#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{} {}{}".format(len(argv) - 1, "arguments" if len(argv) != 2 \
        else "argument", ":" if len(argv) > 1 else "."))
    if len(argv) > 1:
        argsleft = len(argv) - 1
        i = 1
        while argsleft > 0:
            print("{}: {}".format(i, argv[i]))
            argsleft -= 1
            i += 1
    