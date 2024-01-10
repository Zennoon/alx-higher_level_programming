#!/usr/bin/python3
def best_score(a_dict):
    max_score = 0
    max_scorer = None
    if a_dict is not None:
        for key, val in a_dict.items():
            if val > max_score:
                max_scorer, max_score = key, val
    return (max_scorer)


def best_score_2(a_dict):
    if a_dict is not None and len(a_dict) != 0:
        return (max(a_dict))
    return (None)
