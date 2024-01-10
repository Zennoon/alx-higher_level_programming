#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_scores = [score * weight for score, weight in my_list]
    total_weight = 0
    for tup in my_list:
        total_weight += tup[1]
    if total_weight == 0 or len(my_list) == 0 or my_list is None:
        return (0)
    return (sum(weighted_scores) / total_weight)
