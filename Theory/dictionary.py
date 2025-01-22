# part focuses on a specific task.

# def get_bread():
#     print("Getting bread")

# def add_peanut_butter():
#     print("Adding peanut butter")

# def close_sandwich():
#     print("Closing sandwich")

# # Main program
# get_bread()
# add_peanut_butter()
# close_sandwich()

# 6.what happens when function is called?
# when function is called function body is executed.

# 7.what will be the output?
# def f():
# 	s = '-- Inside f()'
# 	print(s)
	
# print('Before calling f()')
# f()
# print('After calling f()')

# 8.what dry principe is?
# dry means don't repeat yourself, which means don't repeat code

# 9.what is stub function?
# when we define function which do nothing it calls stub.to define stub function we use pass which is null operation

# 10.What are positional arguments in Python?
# Positional arguments are arguments passed to a function in the exact order of the parameters.
# give an example

# 11.What is the difference between parameters and arguments?
# parameters are placeholders defined in function, arguments are values passed when calling the function.

# def greet(name, age):
#     print(f"{name} is {age} years old")

# greet('Alice', 30)

# 12.What are keyword arguments in Python?
# keyword arguments are arguments of <key><value>, assigning values to parameters by name

# def f(item, price):
#     print(f'{item} cost {price:.2f}')

# f(item='banana', price=1)

# 13.How do keyword arguments differ from positional arguments?
# the keyword arguments allows to specify arguments in any order

# def f(item, price):
#     print(f'{item} cost {price:.2f}')

# f(price=1, item='mango')

# 14.Can positional and keyword arguments be used together?
# yes but positional arguments must come first, otherwises its syntax error

# def f(item, price):
#     print(f'{item} cost {price:.2f}')

# f('banana', price=1)
# f(price = 2, 'mango')

# 15.What are default parameters in Python?
# default parameters are parameters which has its default value
# give me an example
# def f(item = 'banana', cost = 1):
#     print(f"{item} costs ${cost}")
# f()
# f('mango', 2)
# f(item = "Kiwi", cost = 3)

# 16.Can you specify default parameters using keyword arguments?
# yes default parameters can be specified with keyword arguments
# give me an example 

# def f(qty=6, item='bananas', price=1.74):
#     print(f'{qty} {item} cost ${price:.2f}')

# f(item='Mango')

# 17.Can default parameters be used with positional and keyword arguments?
# yes first must be positional arguments
# give me an example 

# Mutable Default Parameter Values

# DICTIONARIES IN PYTHON
# https://realpython.com/python-dicts/

# 1.Whats dictionary in python?
# Dictionaries are one of python built-in data types, which provides mutable collection of key-value pairs.

# 2.what restrictions have dictionary keys?
# keys should be unique and imutable, thats why we can't use lists as keys.

# 3.how can we create dictionaries in python?
# we can create dictionaries with literals, which are key-value pair in curly braces, also with dict() constructor.


# Task 
# get Ralph, Bob and Sox
# person = {
#     "firstname": "John",
#     "lastname": "Doe",
#     "age": 35,
#     "spouse": "Jane",
#     "children": ["Ralph", "Betty", "Bob"],
#     "pets": {"dog": "Freida", "cat": "Sox"}
# }

# 4. what will happen if you assign new value to an existing key?
# the old value will be overwritten to new value.

# !5.Using a for loop, create a dictionary where each number from 1 to 8 is assigned to its square value. Then, achieve the same 
# result using a dictionary comprehension.

# 6. what get() method do in dictionary?
# it retrieves the value associated with key, if key doesn't exists than it returns default value None

# What will inventory.get("apple") return for inventory =  {"apple": 100, "orange": 80, "banana": 100}?

# What will inventory.get("mango", 0) return in same dictionary?

# 7. what does the values() method do in dictionary?
# it returns dictionary values

# how are duplicate values handled by .values()?
# duplicate values are included as many times as they appear in dictionary

# What will inventory.values() return for inventory = {"apple": 100,  "orange": 80, "banana": 100}?
# dict_values([100, 80, 100])

# What type of object does .values() return?
# dict_values object

# 8. What does the .keys() method do in a dictionary?
# .keys() method returns the keys of dictionary

# What type of object does .keys() return?
# dict_keys object

# What will inventory.keys() return for inventory = {"apple": 100, "orange": 80, "banana": 100}?
# dict_keys(['apple', 'orange', 'banana'])

# 9.What does the .items() method do in a dictionary?
# it returns the key-value pair as tuples in a list

# What type of object does .items() return?
# dict_items object

#  What will inventory.items() return for inventory = {"apple": 100, "orange": 80, "banana": 100}?
# dict_items([(apple, 100), (orange, 80), (banana, 100)])

# 10. What does the .setdefault() method do in a dictionary?
# it retrieves the value if it exists, or it sets velue to default which is None

# What will inventory.setdefault("mango") return for inventory = {"apple": 100, "orange": 80}?

# What will inventory.setdefault("banana", 0) do to the dictionary?
# it will add banana as key and 0 as value

#  inventory = {"apple": 100, "orange": 80} 
# add to inventory mango: None and banana 0 with setdefault() method
# ---------------------------------------------------------------------FROM HERE-----------------------------------------------------
# inventory = {"apple": 100, "orange": 80}
# inventory.setdefault("mango")
# inventory.setdefault("banana", 0)
# print(inventory)

# 11.what does the update() method do in dictionary?
# it merges another dictionary or itarable key-velue pairs into dictionary
# updating existing key or adding new ones.

# Can .update() accept an iterable of key-value pairs?
# yes it can accept iterables like list of tuples 

# Task
# config = {
#     "color": "green",
#     "width": 42,
#     "height": 100,
#     "font": "Courier",
# }

# user_config = {
#     "path": "/home",
#     "color": "red",
#     "font": "Arial",
#     "position": (200, 100),
# }

# merge this dictionaries
# update config with list of tuples 
# update config with keyword arguments

# 12. what pop() method do in dictionary?
# it removes key-value pair by key and returns the value if the key exists

# what happens if key does'n exists and no default value is provided?
# keyError

# what happens if key doesn't exists and default value is provided?
# the value will be returned

# What does inventory.pop("apple") return for inventory = 
# {"apple": 100, "orange": 80}?
# will be returned 100 and removed "apple" from the dictionary

# What will happen when you call inventory.pop("mango", 0) if 
# "mango" isn’t in the dictionary?
# it will return 0 

# How is del different from .pop()?
# del removes key-value pair and not returns value, pop() do same but returns value

# Task
# in inventory = {"apple": 100, "orange":80, "banana":100}
# remove apple and returns its value 
# remove 'mango' 
# remove 'mango' with value 0
# remove banana without returning value

# print(inventory.pop("apple"))
# print(inventory)
# # print(inventory.pop("mango"))
# print(inventory.pop("mango", 0))
# del inventory["banana"]
# print(inventory)

# 13.What does the zip() function do?
# the zip takes iterables as an argument and returns them as combining tuple

# how can you creating dictionary using zip?
# combining the sequences with zip() than pass the result to dict()
# a = ['a', 'b', 'c']
# b = [1, 2, 3, 4]
# dic = dict(zip(a, b))
# print(dic)

# 14.what is the .fromkeys() method's purpose?
# .fromkeys() creates new dictionary from an iterable of keys
# whith the default value None.
# inventory = dict.fromkeys(["apple", "orange", "banana"])
# print(inventory)

# What happens if the input iterable contains duplicate keys?
# duplicate keys will be ignored and final dictionary
# will have unique keys

# inventory = dict.fromkeys(["apple", "banana", "apple"], 0)
# print(inventory)

# what .popitem() method do?
# popitem methos removes and returns key-value pair as a tuple

# What happens if you call .popitem() on an empty dictionary?
# it raises KeyError

# What is the return type of .popitem()?
# tuple 
# inventory = {"apple": 100, "orange":80, "banana": 100}
# print(inventory.popitem())
# print(inventory)
# inventory.popitem()
# print(inventory)
# inventory.popitem()
# inventory.popitem()
# print(inventory)

# 15. inventory = {"apple": 100, "orange":80, "banana": 100}
# clear the inventory
# inventory = {"apple": 100, "orange":80, "banana": 100}
# inventory.clear()
# print(inventory)

# 16.What do the in and not in operators do in dictionaries?
# they check if key, value and key-value is in dictionary

# check if key is in dictionary
# fruits = {'banana': 10, 'apple': 5, 'mango': 8}

# print('banana' in fruits)
# print('apple' in fruits.keys())

# check value in dictionary
# fruits = {'banana': 10, 'apple': 5, 'mango': 8}
# print(10 in fruits.values())
# print(3 in fruits.values())

# check key-value pair in dictionary
# fruits = {'banana': 10, 'apple': 5, 'mango': 8}
# print(('banana', 10) in fruits.items())

# 17.what equality operator do in dictionary?
# equality operator checks if key-value pair is equal
# without order.
# dict1 = {1: 1, 2: 2, 3: 3}
# dict2 = {2: 2, 1: 1, 3: 3}
# print(dict1 == dict2)

#What does the union operator (|) do with dictionaries?
# inion operator creates new dictionary by marging dictionaries
# if keys are same right hand dictionary takes precedence

# config = {"color": "red", "width": 8, "height": 6}
# Merge 3 dictionaries as final result will be 
# {"color": "blue", "width": 8, "height": 7, "path": "home"}

# What does the augmented union operator (|=) do with 
# dictionaries?
# it updates the key-value from another dictionary
# dict1 = {"banana": 8, "apple": 9, "mango": 4}
# dict2 = {"banana": 10, "apple": 4, "ananas": 2}
# update dict1 with augmented operator with dict2

# What is the difference between | and |=?
# | union operator creates new dictionary and |= augmented
# operator updates dictionary in place 

# 18.check if all values are truthy or if at least one is 
# truthy
# fruits = {"apple": 80, "orange": 10, "banana": 0}

# 19. find min and max prices
# items = {"car": 4, 'ball': 8, 'tank': 9}

# 20.sort dictionary with keys, than with values
# than with reverse order
# students = {'Charlie': 8, 'Alice': 5, 'Bob': 15}

# calculate average sales, use sum()
# sales = {'Monday': 8, 'Tuesday': 9, 'Wednesday': 10}

# iterate through key and value
# fruits = {'banana': 8, 'mango': 10, 'grape': 11}

# Exploring Existing Dictionary-Like Classes

# 21. What is the purpose of the Counter class?
# Counter counts objects in elements like list, string or any iterable

# In which module is the Counter class found?
# Counter class found in collections module

# How are the keys and values organized in a Counter?
# the key are elements being counted and the values are the number of occurences of each element

# give the example of counter

# 22.What is the purpose of defaultdict?
# defaultdict automatically creates a key with default value

# What happens when you call departments['Sales'].append('John') and 
# 'Sales' doesn’t exist in the dictionary yet?

# defaultdict automatically creates the 'sales' as a key and a empty list
# and then appends the value 'John' to that list

# What is the main advantage of using defaultdict over a 
# regular dictionary?

# with defaultdict we don't want to manually check the keys

# Task 
# group the department with the defautldict

# employees = [("Sales", "John"),("Sales", "Martin"),("Marketing", "Sara")]

# 23.what are some common methods for working with dictionaries?
# .get() method for retrieving default values, .setdefault() for setting
# default values, .update() for merging dictionaries, .pop() for removing
# keys and .items(), .keys(), .values() for accessing key-values

# 24. how do you iterate over dictionary?
# with using loops. to iterate in keys we use .keys(), in values .values()
# for both of them we use .items(), which yields key-value pairs as tuple.






