#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv)
    if length == 1:
        print("{} arguments.".format(length - 1))
    elif length == 2:
        print("{} argument:".format(length - 1))
        print("{}: {}".format(length - 1, argv[1]))
    elif length > 2:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, argv[i]))
