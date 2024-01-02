#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        printed = ""
        if i % 15 == 0:
            printed = "FizzBuzz"
        elif i % 5 == 0:
            printed = "Buzz"
        elif i % 3 == 0:
            printed = "Fizz"
        else:
            printed = i
        print("{}".format(printed), end=" ")
    print("")
fizzbuzz()
