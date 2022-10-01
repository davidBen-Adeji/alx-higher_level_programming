#!/usr/bin/python3
def uppercase(st):
    string = st
    for c in string:
        asc = ord(c)
        case = asc - 32 if asc >= 97 and asc <= 122 else asc
        print("{:c}".format(case), end="")
    print("")
