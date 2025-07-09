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

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name(mname = "Vaibhav", fname = "Ayush", lname = "Pansare")

""" 
Required arguments:

In case we don't pass the arguments with a key = value 
syntax, then it is necessary to pass the arguments in 
the correct positional order and the number of arguments 
passed should match with actual function definition.

when number of arguments passed does not match to the 
actual function definition. Note:- Will show error
"""
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name("Peter", "Quill")
 
""" 
Variable-length arguments:

Sometimes we may need to pass more arguments than those 
defined in the actual function. This can be done using 
variable-length arguments.

There are two ways to achieve this:
"""

"""
Arbitrary Arguments:

While creating a function, pass a * before the parameter 
name while defining the function. The function accesses 
the arguments by processing them in the form of tuple.
"""

# def name(*name):
#     print("Hello,",name[0], name[1], name[2])

# name("Ayush", "Vaibhav", "Pansare")

"""
Keyword Arbitrary Arguments:

While creating a function, pass a ** before the parameter 
name while defining the function. The function accesses 
the arguments by processing them in the form of dictionary.
"""

# def name(**name):
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Vaibhav", fname = "Ayush", lname = "Pansare")

""" 
return Statement:

The return statement is used to return the value of the expression 
back to the calling function.
"""


# def avg(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + 1
#     return sum / len(numbers)

# a = avg(1, 2, 1, 2, 3, 1)
# print(a)

""" 
Python Lists:

Lists are ordered collection of data items.
They store multiple items in a single variable.
List items are separated by commas and enclosed 
within square brackets [].
Lists are changeable meaning we can alter them 
after creation.
"""

# marks = [10, 9, 7, "Ayush", True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

"""
List Index:

Each item/element in a list has its own unique index. This index can be 
used to access any particular item from the list. The first item has index [0], 
second item has index [1], third item has index [2] and so on.
"""

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# """        [0]      [1]     [2]      [3]      [4]"""

""" 
Accessing list items:

We can access list items by using its index with the square bracket syntax []. 
For example colors[0] will give "Red", colors[1] will give "Green" and so on...
"""

"""Positive Indexing:

As we have seen that list items have index, as such we can access items using these indexes.
"""

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# print(colors[2])
# print(colors[4])
# print(colors[0])

"""
Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, 
but from the end of the list. The last item has index [-1], second last item 
has index [-2], third last item has index [-3] and so on.
"""

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])

"""
Check whether an item in present in the list?

We can check if a given item is present in the list. This is done using the 
in keyword.
"""

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Yellow" in colors:
#     print("Yellow is present.")
# else:
#     print("Yellow is absent.")



