#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Return a list of booleans such that for every number my_list[i], the
    returned list's corresponding element is True if my_list[i] is even, and
    False if it is odd
    """
    return ([num % 2 == 0 for num in my_list])
