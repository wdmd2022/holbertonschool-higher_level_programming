#!/usr/bin/python3
def fizzbuzz():
    for t in range(1, 101):
        if t % 15 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        elif t % 3 != 0 and t % 5 != 0:
            print("{}".format(t), end=" ")
        else:
            print("{}".format("Fizz" if t % 3 == 0 else "Buzz"), end=" ")
