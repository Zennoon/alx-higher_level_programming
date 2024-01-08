#!/usr/bin/python3
def no_c(my_string):
    """
    Return a string that includes all the characters of a given string
    except 'c' and 'C'
    """
    new_string = ""
    if my_string:
        for char in my_string:
            if char != 'c' and char != 'C':
                new_string += char
    return (new_string)
