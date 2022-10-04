#!/usr/bin/python3


def element_at(my_list, idx):
    length = len(my_list)

    if length <= 0 or length <= idx:
        return None

    return my_list[idx]
