More Data Structures: Sets, and Dictionaries

This directory was created on January 10, 2024 for the ALX SE Foundations
sprint #2 project '0x04. Python - More Data Structures: Set, Dictionary'

Set:
A set is an unordered collection of unique elements. Since it is unordered, in
most cases, to iterate into the set, we use the 'in' operator, but using
enumerate is also possible. Sets are usually used when we need a collection
without duplicates, or to test membership. We can create sets using either
the curly braces {}, or the set() function. However, empty sets are created
using the set() function since {} would create an empty dictionary. There are
several operations that can be done on sets like union, intersection,
or difference.

Dictionary:
Dictionaries are collections which are indexed by keys, which can be any
immutable type. The key has to be recursively immutable, meaning it can't be
of a coumpound type that hold a mutable type, like a tuple that contains a list.
We can create dictionaries using key : value pairs in curly braces, or using the
dict() function. We can get the values in a dictionary by using the square
brackets [] notation (like indexing a list but with a key), or using the get()
method. If the key isn't found in the dictionary, the get method by default
(this can be changed by providing a second argument) returns None, while the
brackets notation will raise an error.

Tasks:
