#!/usr/bin/python3
def complex_delete(a_dict, value):
    if a_dict is not None:
        new_dict = a_dict.copy()
        keys = new_dict.keys()
        for key in keys:
            if a_dict.get(key) == value:
                del a_dict[key]
    return (a_dict)
