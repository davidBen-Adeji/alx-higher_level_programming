#!/usr/bin/python3
def remove_char_at(st, n):
    length = len(st)
    string = st

    if n < 0 or n >= length:
        return string
    else:
        return string.replace(string[n], '')
