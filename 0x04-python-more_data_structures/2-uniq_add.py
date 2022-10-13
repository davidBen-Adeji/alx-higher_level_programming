#!/usr/bin/python3


def uniq_add(my_list=[]):
    numbers = set(my_list)
    result = 0
    for item in numbers:
        result += item
    return result
