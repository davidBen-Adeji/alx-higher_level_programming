#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv)
    total = 0
    if length == 1:
        print("{:d}".format(total))
    else:
        for i in range(1, length):
            total += int(argv[i])
        print("{:d}".format(total))
