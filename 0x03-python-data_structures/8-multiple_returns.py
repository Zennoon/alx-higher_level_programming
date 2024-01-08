#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Return the length and first character of a given string.
    If the string is empty, the first character is returned as None
    """
    length = 0
    first_char = None
    if sentence:
        length = len(sentence)
        first_char = sentence[0]
    return (length, first_char)
