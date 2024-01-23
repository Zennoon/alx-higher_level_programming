#!/usr/bin/python3
Square = __import__("3-square").Square

sq1 = Square(3)
print(type(sq1))
print(sq1.__dict__)
print(sq1.area())

sq2 = Square(5)
print(type(sq2))
print(sq2.__dict__)
print(sq2.area())

try:
    print(sq1.size)
except Exception as e:
    print(e)

try:
    print(sq1.__size)
except Exception as e:
    print(e)

try:
    sq3 = Square("3")
    print(type(sq3))
    print(sq3.__dict__)
except Exception as e:
    print(e)

try:
    sq4 = Square(-89)
    print(type(sq4))
    print(sq4.__dict__)
except Exception as e:
    print(e)
