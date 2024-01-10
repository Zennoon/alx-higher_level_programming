#!/usr/bin/python3
def simple_delete(a_dict, key=""):
    a_dict.pop(key, 0)
    return (a_dict)


def simple_delete_2(a_dict, key=""):
    if a_dict.get(key):
        a_dict.pop(key)
    return (a_dict)


def simple_delete_3(a_dict, key=""):
    if a_dict.get(key):
        del a_dict[key]
    return (a_dict)
