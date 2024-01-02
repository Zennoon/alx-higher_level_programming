This directory was created on Jan 2, 2024 to as part of the project
'0x00. Python - Hello, World' of ALX SE Foundations Sprint #2

This project was an introduction to python, and some of its features.
It included such concepts as how to run the interpreter in different ways,
including passing it a python command using the -c command, executing commands
from a file, and others.

0-run: This is a simple shell script that runs a python file whose name is
stored inside an environment variable called 'PYFILE'. One thing that confused
me in this task was why we needed to include the python3 command, because in
the python file, it had the '#!/usr/bin/python3' directive, but I think it is
because if we just write ./$PYFILE, the python file might not be executable
which would result in an error.

1-run_inline: This shell script starts the interpreter kind of in a
non-interactive mode by just passing it a command to run using the -c option.

2-print.py: This script prints exactly \"programming is like building a
multilingual puzzle. The concept that alx wanted us to practice here is mainly
figuring out how to print the quotation marks with print, which is done by
escaping via \.

3-print_number.py: This python script prints a formatted string which includes
a number stored in a variable using f-strings and the print function. The
challenge here is to code defensively. The number variable could be assigned a
string, a list or some other thing. In such a case, we want to throw an error,
hence the d specifier.

4-print_float.py: This script prints a formatted string which interpolates a
float with 2 digits precision using the .2f specifier.

5-print_string.py: This script introduces the concepts of string replication 
using the * operator, and string slicing using indices. It prints a string
stored in a variable 3 times, and then prints the first 9 characters of it.

6-concat.py: This script introduces string concatenation using the + operator.
It concatenates two strings stored in variables along with a space between them.

7-edges.py: This scripts delves further into string slicing, and playing with
negative indices. Instead of using negative indices, the len function could have
been used, but the Zen of Python's third principle is 'Simple is better than
complex'.

8-concat_edges.py: Just another script that slices a single strings and concats
them to form a different sentence.
