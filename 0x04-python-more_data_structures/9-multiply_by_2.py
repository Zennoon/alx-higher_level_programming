#!/usr/bin/python3
def multiply_by_2(a_dict):
    return (dict(map(lambda key: (key, a_dict[key] * 2), a_dict)))


def multiply_by_2_2(a_dict):
    return ({key: val * 2 for key, val in a_dict.items})
