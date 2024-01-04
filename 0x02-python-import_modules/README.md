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
