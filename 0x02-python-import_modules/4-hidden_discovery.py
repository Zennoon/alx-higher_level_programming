#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    defined_names = dir(hidden_4)
    for item in defined_names:
        if item[:2] != "__":
            print(item)
