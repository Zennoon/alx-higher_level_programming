#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as ve:
        stderr.write("Exception: {}\n".format(ve))
        return (False)
