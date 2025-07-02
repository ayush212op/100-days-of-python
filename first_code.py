"""
basic start
"""
# print("Hello World")
# print(5)
# print(17*135)
# print(50+677)
# print(90/9)
# print(70-30)
# print("hi i'm \"ayush\" \n this my first program")
# print("hey",6,7, sep="~", end="ayush\n")

"""
comments:
there two type comments according to the 
number of lines i.e. single and multiline 
comments
"""
# single line comment

"""
multiline 
comment
"""

"""
data types and there initialization using
example
"""
# strings = "Ayush"
# int = 1234567890
# bool = True
# none = None
# float = 4.5
# complex = complex(8,2)
# list = [8, 5], ["ayush","pansare"]
# tuple = ((8, 5),("ayush","pansare"))
# dict = {"Name":"Ayush", "Age":17, "CanVote": False}
"""
check the type here:
"""
# print("the type of", strings, "is",type(strings))
# print("the type of", int, "is",type(int))
# print("the type of", bool, "is",type(bool))
# print("the type of", none, "is",type(none))
# print("the type of", float, "is",type(float))
# print("the type of", complex ,"is",type(complex))
# print("the type of", list, "is",type(list))
# print("the type of", tuple, "is",type(tuple))
# print("the type of", dict, "is",type(dict))

"""
operators
"""
# print(15+6)
# print(15-6)
# print(15*6)
# print(15/6)
# print(15//6)
# print(15%6)
# print(15**3)
"""
example of of printing value of a
variable
"""
# a = 50
# b = 10
# print("the value of",a, "+", b, "is: ", a+b)
# print("the value of",a, "-", b, "is: ", a-b)
# print("the value of",a, "*", b, "is: ", a*b)
# print("the value of",a, "/", b, "is: ", a/b)
"""
type casting
"""
"""
explicit conversion:
The conversion of one data type into 
another data type, done vi developer 
or programmer's intervention or 
manually as per the requirement, 
is known as explicit type conversion.
"""
# var = "1"
# var2 = "2"
# print(var + var2)
# print(int(var) + int(var2)) #explicit
""" functions for explicit conversion:
int(), float(), str(), ord(), hex(),
oct(), tuple(), set(), list(), dict()
"""
"""
Data types in Python do not have the 
same level i.e. ordering of data types 
is not the same in Python. Some of the 
data types have higher-order, and some 
have lower order. While performing any 
operations on variables with different 
data types in Python, one of the 
variable's data types will be changed 
to the higher data type. According 
to the level, one data type is converted 
into other by the Python interpreter 
itself (automatically). This is called, 
implicit typecasting in python.

Python converts a smaller data type 
to a higher data type to prevent data 
loss.
"""
# c = 1.9
# d = 8
# print(c + d)

"""
taking input:
In python, we can take user input 
directly by using input function. 
This input function gives a return value 
as string/character hence we have to 
pass that into a variable
"""

# var3 = input()
# print("my name is: ",var3)

# var4 = int(input())
# print(var4)

# var5 = input("enter your name: ")
# print("your name is: ",var5)

"""
input function just takes input in the 
from of string so we have to convert it if 
we want input as number or an other data 
except string we have to convert it using
explicit conversion
""" 

"""
example: if the input given as a number 
will be stored as a string and if we added 
them without converting it will just 
concatinate the two strings if we add them.
so, we can say it is method of concatinate
that can be use for further applications.
# note this only works with adding and
using other operator will show a error. 
"""
# x = input("Enter the first number: ")
# y = input("Enter the second number: ")
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)
# print(x ** y)
"""
solution:
"""
# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# print(x + y)

"""
Strings:
In python, anything that you enclose 
between single or double quotation 
marks is considered a string. 
A string is essentially a sequence 
or arijay of textual data. Strings 
are used when working with Unicode 
characters
"""
# name = "Harry"
# friend = "Rohan"
# anotherFriend = 'Lovish'

# print("Hello, " + name) # Used concatination
"""
Note: It does not matter whether you 
enclose your strings in single or double 
quotes, the output remains the same.
Sometimes, the user might need to put 
quotation marks in between the strings 
Example, consider the sentence: 
He said, "I want to eat an apple".
How will you print this statement in 
python? We will definitely use single 
quotes for our convenience

Example:
"""
# print('He said, "I want to eat an apple"')

"""
Multiline strings
"""

a = """Lorem ipsum dolor sit amet, 
consectetur adiptactog elit, sed 
do eiusmod tempor incididunt ut 
labore et dolore magna aliqua."""
# print(a)

"""
Accessing Characters of a String:

In Python, string is like an array 
of characters. We can access parts of 
string by using its index which starts 
from D. Square brackets can be used 
to access elements of the string.
"""
# name = "ayush"
# print(name[0])
# print(name[1])
"""
looping through the string:

We can loop through strings using a
for loop like this: 
"""

# for character in a:
#     print(character)
    
"""
String Slicing & Operations on String
"""

"""
String Slicing: 

String slicing in Python allows 
you to extract a portion of a string 
by specifying a start and end index. 
It follows the format 
string[start:end], where start is 
the index where slicing begins 
(inclusive) and end is the index 
where it ends (exclusive).
"""
# fruit = "mango"
'''including 0 but not 3'''
# print(fruit[0:3])
'''including 3 but not 5'''
# print(fruit[3:5])
'''including 0 but not 3 in different way'''
# print(fruit[:3])

'''including 0 but not 3 by 
negative slicing

it's like print(fruit[0:Len(fruit)-2)
'''
# print(fruit[0:-2])
'''including 2 but not 4 by 
negative slicing'''
# print(fruit[-3:-1])


# nm = "ayush"
# print(nm[-4:-2])

"""
Length of a String:

We can find the length of a 
string using len() function. 
"""
# name = input("Enter your name here: ")
# len1 = len(name)
# print("length of your name", name, "is :",len1)

"""
String methods:

Python provides a set of built-in 
methods that we can use to alter and 
modify the strings.

# note: Strings sre immutable, so the
function mentioned below will take the given
string and modify it provide a new
string as an output i.e. OG string
changed
"""

"""
upper():

The upper) method converts a string 
to upper case
"""
# str1 = "AbcHFgR"
# print(str1.upper())

"""
lower()
The lower) method converts a string 
to lower case.
"""

# str1 = "AbcHFgR"
# print(str1.lower())

""" 
rstrip():

the rstrip() removes any trailing 
characters in the string.
"""
# str3 = "!!!Hello !!!!!!"
# print(str3.rstrip("!"))

"""
replace():

The replace() method replaces all 
occurences of a string with another 
string
"""
# str2 = "Silver Spoon"
# print(str2.replace("Sp","H"))

"""
split():

The split() method splits the given 
string at the specified instance 
and returns the separated strings 
as list items.
"""
# str2 = "Silver Spoon"
# print(str2.split(" "))

"""
capitalize():
The capitalize() method turns only 
the first character of the string 
to uppercase and the rest other 
characters of the string are turned 
to lowercase. The string has no 
effect if the first character is 
already uppercase. 
"""

# blogHeading = "introduction to python"
# print(blogHeading.capitalize())

# blogHeadingwrong = "introduction to pyThon"
# print(blogHeading.capitalize())

"""
center():

The center() method aligns the string 
to the center as per the parameters 
given by the user.
"""

# str1 = "Welcome to the Console!!!"
# print(str1.center(50))

'''Explaination'''
# print(len(str1))
# print(len(str1.center(50)))

""" 
count():
The count method returns the number of 
times the given value has occurred 
within the given string.
"""

# str2 = "Abracadabra"
# countStr = str2.count("a")
# print(countStr)

""" 
endswith():

The endswith method checks if the string 
ends with a given alue. If yes then return 
True, else return False
"""
# str3 = "Welcome to the Console!!!"
# print(str3.endswith("!!!"))

'''between a a specific range like 4th character to 9th charater'''
# print(str3.endswith("to", 4,10))

""" 
find():

The find() method searches for the first 
occurrence of the given value and returns 
the index where it is present. If given 
value is absent from the string then return -1.
"""

# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("is"))

'''If not found returns -1'''
# print(str1.find("ishh"))

""" 
index():

The index() method searches for the first 
occurrence of the given value and retums 
the index where it is present. If given value 
is absent from the string then raise an 
exception
"""
# str1 = "He's name is Dan. He is an honest man."
# print(str1.index("is"))
'''If not found returns an error'''
# print(str1.find("ishh"))

""" 
isalnum():
The isalnum method retums True only if the 
entire string only consists of A-Za-z, 0-9. 
If any other characters or punctuations are 
present, then it returns False
"""
# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())

"""
isalpha():

The isalnum() method returns True only 
if the entire string only consists of A-Z 
or -a-z. If any other characters or 
punctuations or numbers(0-9) are present, 
then it returns False.
"""

# str1 = "Welcome"
# print(str1.isalpha())

'''If has a number or punctuations'''
# str1 = "Welcome00.#"
# print(str1.isalpha())

""" 
islower():
The islower() method returns True if all 
the characters in the string are lower 
case, else it returns False,
"""

# str1 = "ayush"
# print(str1.islower())

'''If not lower'''
# str1 = "Ayush"
# print(str1.islower())

""" 
isprintable():
The isprintable() method returns True if 
all the values within the given string 
are printable, if not, then return False.
"""

# str1 = "We wish you a Merry Christmas"
# print(str1.isprintable())

'''If not printable'''
# str1 = "We wish you a Merry Christmas\n"
# print(str1.isprintable())

""" 
isspace():
The isspace() method returns True only and 
only if the string contains white spaces, else returns Faise.
"""

'''using spacbar'''
# str1 = "       "
# print(str1.isspace())

'''using tab'''
# str2 = "        "
# print(str2.isspace())

""" 
istitle():
The istitile returns True only if the 
first letter of each word of the string 
is capitalized, else it returns False
"""

# str1 = "World Health Organization"
# print(str1.istitle())

'''If not'''
# str2 = "To kill the Mocking Bird"
# print(str2.istitle())

"""
isupper():

The isupper() method returns True if 
all the characters in the string are 
upper case, else it returns False
"""

# str1 = "WORLD HEALTH ORGANIZATION"
# print(str1.isupper())

"""
startswith():

The endswith() method checks if the 
string starts with a given value. 
If yes then return True, else return False
"""

# str1 = "Python is a interpreted language"
# print(str1.startswith("Python"))

""" 
swapcase():

The swapcase() method changes the character
casing of the string. Upper case are converted 
to lower case and lower case to upper case.
"""

# str1 = "Python is a interpreted language"
# print(str1.swapcase())

""" 
title():
The title() method capitalizes each letter 
of the word within the string
"""

# str1 = "his manthan and he is a honest man."
# print(str1.title())





"""if-else Statements:
Sometimes the programmer needs to 
check the evaluation of certain 
expression(s), whether the expression(s) 
evaluate to True or False. If the 
expression evaluates to False, then 
the program execution follows a different 
path than it would have if the expression 
had evaluated to True.


Based on this, the conditional statements 
are further classified into following types:

if-else
if-else-elit
nested if-else-elif.
"""

# a = int(input("Enter you age: "))
# print("Your age is",a)
# if(a>18):
#     print("you can drive")
# else:
#     print("You can't drive")
    
'''
Conditional operators: >, <, >=, <=, ==, !=
'''

# print (a > 18)
# print (a <= 18)
# print (a == 18)
# print (a != 18)

""" 
An if......else statement evaluates like this:


if the expression evaluates True:

Execute the block of code inside it statement.
After execution return to the code out of the 
if.....else block.

If the expression evaluates False:
Execute the block of code inside else statement.
After execution return to the code out of the 
if...else block.
"""

# applePrice = 210
# budget = 200
# if (applePrice <= budget):
#     print("Ayush, add 1 kg Apples to the cart.")

# else:
#     print("Ayush, do not add Apples to the cart.")
""" 
elif Statements:

Sometimes, the programmer may want to evaluate 
more than one condition, this can be done using 
an elif statement.
"""

"""
Working of an elif statement:
Execute the block of code inside if statement 
if the initial expression evaluates to True. 
After execution return to the code out of the 
if block.

Execute the block of code inside the first elif 
statement if the expression inside it evaluates 
True. After execution return to the code out of 
the if block.

Execute the block of code inside the second elif 
statement if the expression inside it evaluates 
True. After execution return to the code out of 
the if block.
.
.
.
Execute the block of code inside the nth elif 
statement if the expression inside it evaluates 
True. After execution return to the code out of 
the if block.

Execute the block of code inside else statement 
if none of the expression evaluates to True. 
After execution return to the code out of 
the if block.
"""

# num = int(input("Enter a number: "))
# if (num < 0):
#     print("Number is negative.")
# elif (num == 0):
#     print("Number is Zero.")
# else:
#     print("Number is positive.")

""" 
Nested if statements:
We can use if, if-else, elif statements inside 
other if statements as well.
"""

# num = int(input("Enter the number: "))
# if (num < 0):
#     print("Number is negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")

""" 
code on time packages
"""
# import time
# time_now = int(time.strftime('%H'))
# if(time_now > 6 and time_now < 12): 
#     print("Good morning, SirJi")
    
# elif(time_now > 12 and time_now < 17):
#     print("Good afternoon, SirJi")

# elif(time_now > 17 and time_now < 22):
#     print("Good evening")
# else:
#     print("Good night, SirJi")

"""
Match Case Statements:
To implement switch-case like characteristics very similar 
to if-else functionality, we use a match case in python. 
If you are coming from a C, C++ or Java like language, 
you must have heard of switch-case statements. If this 
is your first language, dont worry as I will tell you 
everything you need to know about match case statements 
in this video!

A match statement will compare a given variable's value 
to different shapes, also referred to as the pattern. 
The main idea is to keep on comparing the variable with 
all the present patterns until it fits into one.

The match case consists of three main entities :

The match keyword
One or more case clauses
Expression for each case

The case clause consists of a pattern to be matched 
to the variable, a condition to be evaluated if the 
pattern matches, and a set of statements to be 
executed if the pattern matches.
"""

# weekdays = int(input("Enter the day: "))

# match(weekdays):
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invaild input!!!")
 

   
"""
Introduction to Loops:
Sometimes a programmer wants to execute a group of 
statements a certain number of times. This can be 
done using loops. Based on this loops are further 
classified into following main types;

for loop
while loop
"""

"""
The for Loop:

for loops can iterate over a sequence of iterable 
objects in python. Iterating over a sequence is 
nothing but iterating over strings, lists, 
tuples, sets and dictionaries.
"""

'''Loop strings'''
# name = "Ayush"
# for i in name:
#     print(i)

'''Loop list'''
# names = ["Ayush" , "Manthan" , "Tanish" , "Shlok"]
# for x in names:
#     print(x)

'''
Loop in range

range():
What if we do not want to iterate over a sequence? 
What if we want to use for loop for a specific number 
of times?

Here, we can use the range() function.
'''

# for r in range(10):
#     print(r)

# for r in range(4,10):
#     print(r)

# for r in range(4,10,2):
    # print(r)

"""
Python while Loop:

As the name suggests, while loops execute statements while 
the condition is True. As soon as the condition becomes False,
the interpreter comes out of the while loop.
"""

# i = 0
# while(i < 20):
#     print(i)
#     i = i + 1

"""
Else with While Loop:

We can even use the else statement with the while loop. 
Essentially what the else statement does is that 
as soon as the while loop condition becomes False, 
the interpreter comes out of the while loop and 
the else statement is executed.
"""
# x = 5
# while (x > 0):
#     print(x)
#     x = x - 1
# else:
#     print('counter is 0')

""" 
Do-While loop in python:

do..while is a loop in which a set of instructions will 
execute at least once (irrespective of the condition) and 
then the repetition of loop's body will depend on the 
condition passed at the end of the while loop. 
It is also known as an exit-controlled loop.

How to emulate do while loop in python?
To create a do while loop in Python, you 
need to modify the while loop a bit in order 
to get similar behavior to a do while loop.

The most common technique to emulate a do-while
loop in Python is to use an infinite while loop
with a break statement wrapped in an if statement
that checks a given condition and breaks the 
iteration if that condition becomes true:
"""

# while True:
#     str = input("Enter a specific string(type 'H' to end)")
#     print(str)
#     if str == "H":
#         break

# while True:
#   number = int(input("Enter a positive number: "))
#   print(number)
#   if not number > 0:
#     break

'''infinite loop to print number'''
# i = 0
# while True:
#     print(i)
#     i = i + 1

'''Same program emulated to do while loop'''
# i = 0
# while True:
#     print(i)
#     i = i +1
#     if(i%100 == 0):
#         break

"""
break statement:

The break statement enables a program to skip over a part 
of the code. A break statement terminates the very loop it lies within.
"""

# for i in range(1,101,1):
#     print(i ,end=" ")
#     if(i==50):
#         break
#     else:
#         print("Mississippi")
# print("Thank you")

"""
Continue Statement:
The continue statement skips the rest of the 
loop statements and causes the next iteration to occur.
"""

for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

""" 
Python Functions:

A function is a block of code that performs a specific 
task whenever it is called. In bigger programs, where 
we have large amounts of code, it is advisable to create 
or use existing functions that make the program flow 
organized and neat.

There are two types of functions:

Built-in functions
User-defined functions

"""

"""
Built-in functions:

These functions are defined and pre-coded in python. 
Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), 
list(), tuple(), set(), print(), etc.

User-defined functions:
We can create functions to perform specific tasks as 
per our needs. Such functions are called user-defined 
functions.

Syntax:
def function_name(parameters):
  pass
  # Code and Statements
  
Create a function using the def keyword, followed 
by a function name, followed by a paranthesis (()) and 
a colon(:).

Any parameters and arguments should be placed within 
the parentheses.Rules to naming function are similar 
to that of naming variables. Any statements and other 
code within the function should be indented.
"""

"""
Calling a function:
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.
"""

def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)

c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)

