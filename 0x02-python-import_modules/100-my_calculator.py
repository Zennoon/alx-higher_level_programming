#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    operators = ['+', '-', '*', '/']
    funcs = [add, sub, mul, div]
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    handler_func = funcs[operators.index(argv[2])]
    result = handler_func(int(argv[1]), int(argv[3]))
    print("{:s} {:s} {:s} = {:d}".format(argv[1], argv[2], argv[3], result))
