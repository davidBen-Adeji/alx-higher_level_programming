#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    score_sum = sum([score * weight for (score, weight) in my_list])
    weight_sum = sum([weight for (score, weight) in my_list])
    weight_avg = score_sum / weight_sum

    return weight_avg
