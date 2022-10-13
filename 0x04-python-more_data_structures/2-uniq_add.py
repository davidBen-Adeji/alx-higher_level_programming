#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    numbers = set(my_list)
    result = reduce(lambda a, b: a + b, numbers)
    return result
