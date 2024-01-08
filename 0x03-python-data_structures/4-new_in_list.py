#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a given position without modifying the
    original list.
    """
    if my_list:
        new_list = my_list.copy()
        if idx >= 0 and idx < len(new_list):
            new_list[idx] = element
        return (new_list)
