#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a, b = int(argv[1]), int(argv[3])
op = argv[2]

if op not in ['+', '-', '*', '/']:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
if op == '+':
    res = add(a, b)
elif op == '-':
    res = sub(a, b)
elif op == '*':
    res = mul(a, b)
elif op == '/':
    res = div(a, b)

print("{} {} {} = {}".format(a, op, b, res))
