#!/usr/bin/python3
def no_c(my_string):
    """
    Return a string that includes all the characters of a given string
    except 'c' and 'C'
    """
    if my_string:
        char_list = [char for char in my_string if char not in "Cc"]
        return ("".join(char_list))
