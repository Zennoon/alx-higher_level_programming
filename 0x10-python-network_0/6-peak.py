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
    mid = len(list_int) // 2
    if (mid - 1) >= 0 and list_int[mid - 1] > list_int[mid]:
        return (find_peak(list_int[0:mid]))
    if (mid + 1) < len(list_int) and list_int[mid + 1] > list_int[mid]:
        return (find_peak(list_int[mid + 1:]))
    return (list_int[mid])


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
