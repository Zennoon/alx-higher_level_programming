#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""5-text_indentation.py

Author: Yunus Kedir

This module holds a function that prints the individual sentences in a text
separated by one blank line. The tests for this module can be found inside
the tests directory in the 5-text_indentation.txt file. They were implemented
using doctest.

"""


def text_indentation(text):
    """Prints the individual sentences in a given text separated by a blank
    line.

    For the purposes of this function, a sentence is considered as a piece of
    text between any of these delimiters (., ?, and :) except any whitespace
    at the beginning and ending.

    The function also performs validation on the given text.
    The text must be a string.

    Args:
        text (str): The text which is parsed into sentences.
    """
    if text.__class__ is not str:
        raise TypeError("text must be a string")
    leng = len(text)
    start = 0
    end = 0
    while start < leng and text[start:].strip():
        while end < leng and text[end] not in ".?:":
            end += 1
        if end < leng:
            sentence = text[start:end + 1].strip()
            print(sentence + '\n')
        else:
            sentence = text[start:end].strip()
            print(sentence, end="")
        end += 1
        start = end
