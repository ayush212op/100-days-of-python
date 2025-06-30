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
assignment operator
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

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())