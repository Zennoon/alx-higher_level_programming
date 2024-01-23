#!/usr/bin/python3
Square = __import__("6-square").Square

sq = Square(9, (3, 3))
print("Area: {} for size: {}".format(sq.area(), sq.size))
sq.my_print()
print("--------------------------------------------------------")
sq.size = 0
sq.my_print()
print("--------------------------------------------------------")
sq.size = 3
sq.position = (0, 0)
print("Area: {} for size: {}".format(sq.area(), sq.size))
sq.my_print()
try:
   sq.size = "5 feet"
   print("Area: {} for size: {}".format(sq.area(), sq.size))
except Exception as e:
   print(e)
