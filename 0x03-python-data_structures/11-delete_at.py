#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Delete the element at a given index of a given list if possible and return
    the list.
    """
    if my_list and idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
