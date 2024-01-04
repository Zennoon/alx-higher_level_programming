Import & Modules

This directory was created on January 4, 2024 for the ALX SE Foundation
sprint #2 project '0x02. Python - import & modules'

Modules:
When a program gets larger, it is probably best to logically split it into
different files for better maintainability and clarity. Once we've done that,
there has to be a way through which we can use functions, variables, and classes
defined inside one file in another file.
Another scenario is when we have a really useful function that we use in many
programs, but defining the function in every file and program would beat the
purpose of functions being reusable blocks of code.

This is where modules in python come in. Modules are python files that have
functions, variables, classes, expressions, or combination of those defined
inside. We can then import these modules using the <strong>import</strong>
keyword. This allows us to use the things defined in the module in another
file. This importing file could be a script or a module itself.

There are different variants we could use to import modules.
1. import modulename

This statement adds the module name into the namespace of the importing file,
and through this name, we can access, or even modify the things defined in the
module. The things defined in the modules are not added themselves, only the
module name. We can access a function, funcname inside the module as
modulename.funcname.

2. from modulename import ...

When using this variant, all the names that we state after the import keyword
are imported/added to the namespace of the importing script/module. However, the
module name itself is not added. In this scenario, we are able to use the
imported functions/variables/classes, but we are not modify the definition found
in the module. It is sort of like using a copy of them. We can alter the copies,
but not the ones in the module.

When importing a module, the expressions inside are executed once. But what if
don't want them to execute when the module is imported? We can use __name__.
__name__ is a global variable that holds the name of the file. One exception is
when the file is the main file, meaning it is the script that is given to the
interpreter and it is not imported. In such cases, the __name__ variable holds
the value '__main__'. We can use this as an if condition to execute certain
expressions only when the script is the main one, and not a module being
imported.

Tasks:
0-add.py: This script just imports a single function called add from a file
called add_0.py. The challenge here is to make the code not execute when
imported using the __name__ trick.

1-calculation.py: Imports multiple functions and executes them by passing
local variables as arguments.

2-args.py: This script gets the command line arguments list with sys.argv
and prints them if any.

3-infinite_sum: This one is essentially for the most part the same as the above,
the only difference being instead of printing the arguments, we convert them to
ints (it is assumed that they can all be casted using int()) and add them and
then print the sum.

4-hidden_discovery: This script imports a compiled python file (.pyc extension)
and prints all the names defined by the file using the dir() function.

5-variable_load.py: The new thing here is that we are loading a variable instead
of a function from a module.

100-my_calculator.py: This was a bit fun. Gave me a chance to try the function
pointer stuff I learned with C in python, and it turns out that we can actually
store functions (or at least their names) in lists. The script basically accepts
an expression from the command line. If the expression is invalid, it prints an
appropriate message and exits (using sys.exit). Otherwise, we have two lists,
one of the operator signs, and the other of handler function for each operator.
The function handling each operator is placed in the same index in that list
as the operator it handles is placed in the operator signs list. So, once we
identify the index of the operator we receive from the command line, we execute
the function at that index in the functions list. This is done using the index()
method.

101-easy_print.py: This one is quite funny. The challenge was to write the
string "#pythoniscool" with out using 'print' and 'import sys' in the file
and the file has to be 2 lines, and I just thought it was bizarre how the
instructions emphasized the in the file part, and I just wrote the code in
another file and imported that file to my main file. When modules are imported,
the expressions inside them are executed once, so by just importing the module,
I am able to execute the expression.

103-fast_alphabet.py: The challenge here was to print the Uppercase alphabet
characters without using any loop or string literal, and the file can only be
3 lines long. After looking around a bit, I found out about the string module,
and specifically the ascii_uppercase constant, which holds the entire alphabet
in uppercase.
