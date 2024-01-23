#!/usr/bin/python3
Square = __import__("4-square").Square

sq = Square(89)
print("Area: {} for size: {}".format(sq.area(), sq.size))

sq.size = 3
print("Area: {} for size: {}".format(sq.area(), sq.size))

try:
    sq.size = "5 feet"
    print("Area: {} for size: {}".format(sq.area(), sq.size))
except Exception as e:
    print(e)
