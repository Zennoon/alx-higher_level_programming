#!/usr/bin/python3
def print_sorted_dictionary(a_dict):
    sorted_keys = sorted(a_dict.keys())
    list(map(lambda key: print(f"{key}: {a_dict.get(key)}"), sorted_keys))
