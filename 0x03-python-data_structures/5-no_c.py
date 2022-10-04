#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    length = len(my_string)

    if length <= 0:
        return

    for i in range(length):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        else:
            new_string += my_string[i]

    return new_string
