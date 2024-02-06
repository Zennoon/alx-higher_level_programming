#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""7-add_item.py

This script contains:


Functions:
    main - Extracts the command line arguments, adds them to a list and saves
           them to a file

"""


import sys


def main():
    """Adds the command line arguments to a list stored in the add_item.json
    file as a JSON string. The arguments are appended to the list.

    The list is first created using the load_from_json_file function from the
    6-load_from_json_file module. The command line arguments are appended, and
    then the list is restored to the file as a JSON string.
    """
    load_from_file = __import__("6-load_from_json_file").load_from_json_file
    save_to_file = __import__("5-save_to_json_file").save_to_json_file
    args = sys.argv

    with open("add_item.json", 'a', encoding="utf-8") as file_append, \
         open("add_item.json", 'r', encoding="utf-8") as file_read:
        if file_read.read() == "":
            my_list = []
        else:
            my_list = load_from_file("add_item.json")
        my_list.extend(args[1:])
        save_to_file(my_list, "add_item.json")


main()
