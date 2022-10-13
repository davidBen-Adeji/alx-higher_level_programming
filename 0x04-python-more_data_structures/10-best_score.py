#!/usr/bin/python3


def best_score(a_dictionary):
    max_value = -1
    dict_winner = None

    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                dict_winner = key

    return dict_winner
