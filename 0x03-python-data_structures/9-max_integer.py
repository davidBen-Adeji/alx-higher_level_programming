#!/usr/bin/python3


def max_integer(my_list=[]):
    length = len(my_list)
    max_int = 0
    if length == 0:
        return None

    for item in my_list:
        if item > max_int:
            max_int = item

    return max_int
