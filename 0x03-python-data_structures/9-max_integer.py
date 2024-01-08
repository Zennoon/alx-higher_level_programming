#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Return the biggest integer in a list, or None if the list is empty.
    """
    if my_list:
        new_list = my_list.copy()
        new_list.sort(reverse=True)
        return (new_list[0])
    return (None)
