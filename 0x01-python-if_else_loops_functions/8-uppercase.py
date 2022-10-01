#!/usr/bin/python3
def uppercase(st):
    string = st
    for c in string:
        asc = ord(c)
        if asc >= 97 and asc <= 122:
            asc -= 32
            print("{:c}".format(asc), end="")
        else:
            print("{:c}".format(asc), end="")
    print("")
