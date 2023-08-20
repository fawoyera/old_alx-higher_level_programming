#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weighted_score = 0
    total_weight = 0
    for tup in my_list:
        score, weight = tup
        weighted_score += score * weight
        total_weight += weight
    return weighted_score / total_weight
