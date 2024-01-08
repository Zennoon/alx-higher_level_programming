#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            if row:
                for i in range(len(row)):
                    print("{:d}".format(row[i]), end="")
                    if i != len(row) - 1:
                        print(" ", end="")
            print()
