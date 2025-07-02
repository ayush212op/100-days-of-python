"""
Function Arguments and return statement:

There are four types of arguments that we can 
provide in a function:

Default Arguments
Keyword Arguments
Variable length Arguments
Required Arguments
"""

"""
Default arguments:

We can provide a default value while creating 
a function. This way the function assumes a 
default value even if a value is not provided 
in the function call for that argument.
"""

# def average(a = 1, b = 3):
#     print("The average of the two is:",(a/b)/2)

'''Can also change the value of the arguments even 
after declaring the default arguement'''

# average(4)

# def name(fname = "Ayush", mname = "Vaibhav", lname = "Pansare"):
#     print("Hello,", fname, mname, lname)

# name()

"""
Keyword arguments:

We can provide arguments with key = value, this 
way the interpreter recognizes the arguments by 
the parameter name. Hence, the the order in which 
the arguments are passed does not matter.
"""

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname = "Vaibhav", fname = "Ayush", lname = "Pansare")

""" 
Required arguments:

In case we don't pass the arguments with a key = value 
syntax, then it is necessary to pass the arguments in 
the correct positional order and the number of arguments 
passed should match with actual function definition.

when number of arguments passed does not match to the 
actual function definition. Note:- Will show error
"""
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Quill")

