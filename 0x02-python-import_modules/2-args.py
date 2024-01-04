#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    print("{:d}".format(argc - 1), end=" ")
    if argc == 1:
        print("arguments.")
    elif argc == 2:
        print("argument:")
    else:
        print("arguments:")
    for index, arg in enumerate(argv[1:]):
        print("{:d}: {:s}".format(index + 1, arg))
