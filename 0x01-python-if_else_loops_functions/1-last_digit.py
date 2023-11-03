#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if number < 0:
    num *= -1
if num == 0:
    print("Last digit of", number, "is", num, end=" ")
    print("and is 0")
elif number > 0:
    print("Last digit of", number, "is", end=" ")
    if num > 5:
        print(f"{num} and is greater than 5")
    else:
        print(f"{num} and is less than 6 and not 0")
elif num < 0:
    print("Last digit of ", end="")
    print(number, " is ", -(10 - (number % 10)), end=" ", sep="")
    print("and is less than 6 and not 0")
