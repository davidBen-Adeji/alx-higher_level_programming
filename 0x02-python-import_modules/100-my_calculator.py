#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()

length = len(argv)
if length != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(argv[1])
b = int(argv[3])
op = argv[2]

if op == "+":
    print("{:d} {} {:d} = {:d}".format(a, op, b, a + b))
elif op == "-":
    print("{:d} {} {:d} = {:d}".format(a, op, b, a - b))
elif op == "*":
    print("{:d} {} {:d} = {:d}".format(a, op, b, a * b))
elif op == "/":
    print("{:d} {} {:d} = {:d}".format(a, op, b, a / b))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
