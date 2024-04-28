#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Functions:
        find_peak - Finds a peak of an unsorted list of integers

"""


def find_peak(list_int):
    """Finds a peak of an unsorted list of integers.

    A peak is an element which is greater than both its neighbors.
    A list can have more than one peaks. This function returns a single one.

    Args:
        list_int (list<int>): The list of integers a peak of whose is returned.

    Returns:
        Returns: (int) A peak of the list if it has one.
    """
    if len(list_int) == 0:
        return (None)
    size = len(list_int)
    mid = 0
    diff = size // 2
    while not ((mid - 1 < 0 or list_int[mid] >= list_int[mid - 1]) and
               (mid + 1 >= size or list_int[mid] >= list_int[mid + 1])):
        if diff == 0:
            diff = 1
        if mid - 1 >= 0 and list_int[mid - 1] > list_int[mid]:
            mid -= diff
        elif mid + 1 < size and list_int[mid + 1] > list_int[mid]:
            mid += diff
        diff //= 2
    return (list_int[mid])
