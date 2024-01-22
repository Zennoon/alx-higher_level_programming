Exceptions
This directory was created on January 22, 2024 as part of the ALX SE Foundations
project '0x05. Python - Exceptions'.

Exceptions
Exceptions are one type of error that is not syntatical, is caused on execution
(runtime) and is not unconditionally fatal. Although some exceptions are better
off playing out and perhaps halting the program, we might wish to catch and
handle execptions in our code. To achieve this, we use a try - except statement.
The try clause holds the code which is susceptible to be erronous. In our except
clause, we place code to be executed if the try clause does raise an exception,
and the exception is the same type or atleast a derivitve of the one we place in
the except statement. If we have code we want to execute if the exception isn't
raised, we place that in an else clause. Finally, if we have code that we need
to execute regardless of whether the exception was raised or not, we use a \
finally clause.

BaseException: is the base class of all exceptions.
Exception: inherits from BaseException and is the base class for all non-fatal
exceptions.

To create a custom/user-defined exception, we create a class that inherits from
the Exception class (in most cases), and we can initialize it, give it a __str__
method and all sorts of stuff.
