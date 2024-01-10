#!/usr/bin/python3
def roman_to_int(roman):
    arabic = 0
    if type(roman) is not str or roman is None:
        return (arabic)
    for idx in range(len(roman)):
        rest = set(roman[idx:])
        if roman[idx] == 'M':
            arabic += 1000
        elif roman[idx] == 'D':
            if 'M' in rest:
                arabic -= 500
            else:
                arabic += 500
        elif roman[idx] == 'C':
            if 'M' in rest or 'D' in rest:
                arabic -= 100
            else:
                arabic += 100
        elif roman[idx] == 'L':
            if 'M' in rest or 'D' in rest or 'C' in rest:
                arabic -= 50
            else:
                arabic += 50
        elif roman[idx] == 'X':
            if ('M' in rest or 'D' in rest
                    or 'C' in rest or 'L' in rest):
                arabic -= 10
            else:
                arabic += 10
        elif roman[idx] == 'V':
            if ('M' in rest or 'D' in rest or 'C' in rest
                    or 'L' in rest or 'X' in rest):
                arabic -= 5
            else:
                arabic += 5
        elif roman[idx] == 'I':
            if ('M' in rest or 'D' in rest or 'C' in rest
                    or 'L' in rest or 'X' in rest or 'V' in rest):
                arabic -= 1
            else:
                arabic += 1
    return (arabic)
