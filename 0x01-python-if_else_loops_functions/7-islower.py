#!/usr/bin/python3

def islower(c):
    string = ord(c)
    result = False

    for i in range(97, 123):
        if i == string:
            result = True
            break

    return result
