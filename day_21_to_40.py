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

# if "ay" in "ayush":
#     print("yes")

""" 
Range of Index:
You can print a range of list items by specifying where you want to start, 
where do you want to end and if you want to skip elements in between the range.

Syntax:

listName[start : end : jumpIndex]
"""

'''printing elements within a particular range:'''
# marks = [10, 9, 7, 4, 10, 5]
# print(marks[1:-1])
# print(marks[:6])
# print(marks[0:6:2])
# print(marks[-6:-2])


'''printing all element from a given index till the end'''
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[4:])
# print(animals[-4:])

'''printing all elements from start to a given index'''
# print(animals[:5])
# print(animals[:-5])

'''Printing alternate values'''
# print(animals[::2])
# print(animals[-8:-1:2])

""" 
List Comprehension
List comprehensions are used for creating new lists from other iterables like 
lists, tuples, dictionaries, sets, and even in arrays and strings.

Syntax:
List = [Expression(item) for item in iterable if Condition]

Expression: It is the item which is being iterated.

Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

Condition: Condition checks if the item should be added to the new list or not.
"""

# lst = [i for i in range(10)]
# print(lst)

'''Accepts items with the small letter “o” in the new list'''
# name_friends = ["ayush", "mathan", "tanish", "shlok", "prabhudha"]
# name_friends_1 = [name for name in name_friends if "a" in name]
# print(name_friends_1)
'''Accepts items which have more than 4 letters'''
# name_friends_2 = [name for name in name_friends if len(name) > 5]
# print(name_friends_2)




"""List Methods"""

'''append(): This method is used to add more elements at the 
end of the list only'''

# name_friends = ["ayush", "mathan", "tanish", "shlok", "prabhudha"]
# name_friends.append("suraj")
# print(name_friends)

# num = [5,6,4,6,56,7,86,8,980,7,67]
# num.append(3567586)
# print(num)



'''list.sort(): This method sorts the list in ascending order. 
The original list is updated'''

# name_friends = ["ayush", "mathan", "tanish", "shlok", "prabhudha"]
# name_friends.sort()
# print(name_friends)

# num = [5,6,4,6,56,7,86,8,980,7,67]
# num.sort()
# print(num)

'''reverse sorted lists'''
# name_friends = ["ayush", "mathan", "tanish", "shlok", "prabhudha"]
# name_friends.sort(reverse=True)
# print(name_friends)

# num = [5,6,4,6,56,7,86,8,980,7,67]
# num.sort(reverse=True)
# print(num)

'''reverse(): This method reverses the order of the list.'''

# name_friends = ["ayush", "mathan", "tanish", "shlok", "prabhudha"]
# name_friends.reverse()
# print(name_friends)

# num = [5,6,4,6,56,7,86,8,980,7,67]
# num.reverse()
# print(num)

'''index(): This method returns the index of the first occurrence of the list item.'''

# name_friends = ["ayush", "mathan", "tanish", "shlok", "prabhudha"]
# print(name_friends.index("ayush"))

# num = [5,6,4,6,56,7,86,8,980,7,67]
# print(num.index(86))

'''count(): Returns the count of the number of items with the given value.'''

# colors = ["voilet", "green", "indigo", "blue", "green"]
# print(colors.count("green"))

# num = [2, 2, 3, 5, 2, 7, 5, 4, 9, 2]
# print(num.count(2))

'''copy(): Returns copy of the list. This can be done to perform operations 
# on the list without modifying the original list.'''

# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)

'''insert(): This method inserts an item at the given index. User has to specify 
index and the item to be inserted within the insert() method.'''

# name_friends = ["ayush", "mathan", "tanish", "shlok", "prabhudha"]
# name_friends.insert(2, "swaraj")
# print(name_friends)

'''extend(): This method adds an entire list or any other collection datatype 
(set, tuple, dictionary) to the existing list.'''

# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)

'''Concatenating two lists: You can simply concatenate two lists to join two lists.'''

# colors = ["voilet", "indigo", "blue", "green"]
# colors2 = ["yellow", "orange", "red"]
# print(colors + colors2)

"""Python Tuples
Tuples are ordered collection of data items. They store multiple items in a single 
variable. Tuple items are separated by commas and enclosed within round brackets (). 
Tuples are unchangeable meaning we can not alter them after creation.
"""
# tup = (4345, 87666, 7668, 88, 867, 7708)
# print(type(tup), tup)
# print(tup[0])
# print(tup[1])
# print(tup[-1])

# if 4345 in tup:
#     print("yes")
    
    
""" 
Tuple Indexes:

Each item/element in a tuple has its own unique index. This index can be used 
to access any particular item from the tuple. The first item has index [0], 
second item has index [1], third item has index [2] and so on.
"""

"""
Accessing tuple items:
"""
'''Positive Indexing: As we have seen that tuple items have index, as such we can 
access items using these indexes.'''

# country = ("Spain", "Italy", "India",)
# #            [0]      [1]      [2]     
# print(country[0])
# print(country[1])
# print(country[2])

'''Negative Indexing: Similar to positive indexing, negative indexing is also used 
to access items, but from the end of the tuple. The last item has index [-1], second 
last item has index [-2], third last item has index [-3] and so on.
'''


# country = ("Spain", "Italy", "India", "England", "Germany")
# #            [0]      [1]      [2]       [3]        [4]
# print(country[-1]) # Similar to print(country[len(country) - 1])
# print(country[-3])
# print(country[-4])

'''Check for item: We can check if a given item is present in the tuple. This is done 
using the in keyword.'''

# country = ("Spain", "Italy", "India", "England", "Germany")
# if "Germany" in country:
#     print("Germany is present.")
# else:
#     print("Germany is absent.")

# country = ("Spain", "Italy", "India", "England", "Germany")
# if "Russia" in country:
#     print("Russia is present.")
# else:
#     print("Russia is absent.")

'''Range of Index: You can print a range of tuple items by specifying where do you want 
to start, where do you want to end and if you want to skip elements in between the range.

Syntax:
Tuple[start : end : jumpIndex]
Note: jump Index is optional. We will see this in given examples.
'''

'''Example: Printing elements within a particular range:'''
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[3:7])
# print(animals[-7:-2])

'''Example: Printing all element from a given index till the end'''
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[4:])
# print(animals[-4:])

'''Example: printing all elements from start to a given index'''
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[:6])
# print(animals[:-3])


'''Example: Print alternate values'''
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[::2])
# print(animals[-8:-1:2])

'''Example: printing every 3rd consecutive withing given range'''
# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[1:8:3])

""" 
Manipulating Tuples;

Tuples are immutable, hence if you want to add, remove or 
change tuple items, then first you must convert the tuple to a 
list. Then perform operation on that list and convert it back 
to tuple.
"""

# countries = ("India", "Russia", "England", "Itay", "Germany")
# con_list = list(countries)
# con_list.append("Japan")
# con_list.remove("Russia")
# con_list.insert(1, "USA")

# new_con = tuple(con_list)
# print(new_con)

# print(new_con.index("Japan"))
# print(new_con.count("Japan"))

'''concatenate two tuples without converting them to list.'''
# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

"""
Tuple methods:

As tuple is immutable type of collection of elements it have 
limited built in methods.They are explained below
"""
'''count() Method: The count() method of Tuple returns the 
number of times the given element appears in the tuple.'''

# tup = (2, 3, 4, 6, 5, 6, 8, 8, 7, 8, 9, 0)
# print(tup.count(8))

'''index() method: The Index() method returns the first 
occurrence of the given element from the tuple.'''

# tup = (2, 3, 4, 6, 5, 6, 8, 8, 7, 8, 9, 0)
# print(tup.index(5))

# tup = (2, 3, 4, 6, 5, 6, 8, 8, 7, 8, 9, 0)
# print(tup.index(8, 6, 8))

'''len() method: The len() method returns the length of tuple'''

# tup = (2, 3, 4, 6, 5, 6, 8, 8, 7, 8, 9, 0)
# print(len(tup))

"""KBC EXCERCISE"""
'''kbc_question = [
    {"Question": "What is the Capital of India?",
     "Options": ["A. Mumbai", "B. Chennai", "C. New Delhi", "D. Kolkata"],
     "Answer": "C"},

    {"Question": "Which animal is named as 'Ship of the Desert'?",
     "Options": ["A. Horse", "B. Camel", "C. Elephant", "D. Donkey"],
     "Answer": "B"},

    {"Question": "Which festival is known as the 'Festival Of Lights'?",
     "Options": ["A. Holi", "B. Diwali", "C. Eid", "D. Baisakhi"],
     "Answer": "B"},

    {"Question": "What is 5 + 7?",
     "Options": ["A. 10", "B. 11", "C. 12", "D. 13"],
     "Answer": "C"},

    {"Question": "Which planet is known as the Red Planet?",
     "Options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
     "Answer": "C"},

    {"Question": "Who wrote the Indian National Anthem?",
     "Options": ["A. Mahatma Gandhi", "B. Rabindranath Tagore", "C. Jawaharlal Nehru", "D. Subhas Chandra Bose"],
     "Answer": "B"},

    {"Question": "What is the smallest Prime number?",
     "Options": ["A. 0", "B. 1", "C. 2", "D. 3"],
     "Answer": "C"},

    {"Question": "Which is the longest river in India?",
     "Options": ["A. Ganga", "B. Yamuna", "C. Godavari", "D. Brahmaputra"],
     "Answer": "A"},

    {"Question": "Who was the first President of India?",
     "Options": ["A. Sardar Patel", "B. Rajendra Prasad", "C. Radhakrishnan", "D. Zakir Hussain"],
     "Answer": "B"},

    {"Question": "Which organ purifies our blood?",
     "Options": ["A. Heart", "B. Liver", "C. Lungs", "D. Kidney"],
     "Answer": "D"},

    {"Question": "Who is known as the father of the Indian Constitution?",
     "Options": ["A. B.R. Ambedkar", "B. Jawaharlal Nehru", "C. Mahatma Gandhi", "D. Rajendra Prasad"],
     "Answer": "A"},

    {"Question": "Which gas do plants absorb from the atmosphere?",
     "Options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
     "Answer": "C"},

    {"Question": "What is the chemical symbol for gold?",
     "Options": ["A. Gd", "B. Au", "C. Ag", "D. Go"],
     "Answer": "B"},

    {"Question": "In which year did India become a Republic?",
     "Options": ["A. 1947", "B. 1948", "C. 1950", "D. 1952"],
     "Answer": "C"},

    {"Question": "Who is the current Chief Justice of India?",
     "Options": ["A. U.U. Lalit", "B. N.V. Ramana", "C. Bhushan Gavai", "D. Ranjan Gogoi"],
     "Answer": "C"}
]

# Prize ladder
prizes = [
    1000, 2000, 3000, 5000, 10000,
    20000, 40000, 80000, 160000, 320000,
    640000, 1250000, 2500000, 5000000, 10000000
]

print("🎉 Welcome to KBC in Python 🎉\n")

score = 0

for i, question in enumerate(kbc_question):
    print("Q", i + 1, ":", question["Question"])
    for opt in question["Options"]:
        print(opt)

    user_input = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_input == question["Answer"]:
        score = prizes[i]
        print("✅ Correct! You have won ₹" + str(score) + "\n")
    else:
        print("❌ Wrong! The correct answer was:", question["Answer"])
        print("💰 You take home ₹" + str(score))
        break

else:
    print("🎊 Congratulations! You answered all questions correctly!")

print("\n🏆 Total amount won: ₹" + str(score))
print("🙏 Thank you for playing KBC!\n")
'''