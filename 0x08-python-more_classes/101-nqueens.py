#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""101-nqueens.py

"""

import sys


def find_solutions(n):
    solutions = []
    factor = 2
    starter = 1
    for i in range(n - 2):
        solution = []
        y = starter
        for x in range(n):
            if y >= n:
                y = y - 1 - n
            solution.append([x, y])
            y += factor
        starter += 1
        factor += 1
        solutions.append(solution)
    return (solutions)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = find_solutions(n)
    for solution in solutions:
        print(solution)

main()
