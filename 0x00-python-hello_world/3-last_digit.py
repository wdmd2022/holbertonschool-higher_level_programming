#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = number % -10
else:
    digit = number % 10
print("Last digit of {} is {} ".format(number, digit), end="")
if digit == 0:
    print("and is 0")
elif digit < 6:
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")
