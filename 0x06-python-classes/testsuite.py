#!/usr/bin/python3
Square = __import__("102-square").Square

sq1 = Square(5)
sq2 = Square(6)

if sq1 > sq2:
    print("Sq 5 > Sq 6")
if sq1 >= sq2:
    print("Sq 5 >= Sq 6")
if sq1 == sq2:
    print("Sq 5 == Sq 6")
if sq1 != sq2:
    print("Sq 5 != Sq 6")
if sq1 <= sq2:
    print("Sq 5 <= Sq 6")
if sq1 < sq2:
    print("Sq 5 < Sq 6")
