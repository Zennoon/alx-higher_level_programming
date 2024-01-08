#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Print the elements of a given integer list in reverse.
    """
    if my_list:
        my_list.reverse()
        for num in my_list:
            print("{:d}".format(num))
        my_list.reverse()
