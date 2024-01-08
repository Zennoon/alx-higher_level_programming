#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace the element at a given index of a given list with a given value
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
