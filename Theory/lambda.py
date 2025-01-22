# 1. What is a lambda function in Python?
# lambda function is an anonymous function defined using the lambda keyword

# 2. What are the components of a lambda expression?
# keyword: lambda, bound variables: arguments, body: single expression that is computed and returned

# 3. How does a lambda function differ from a regular function?
# lambda function: has no name(anonymous), defined in a single line, containts only one expression in the body

# 4. How do you define and use a lambda function that returns its argument?

# identity = lambda x: x
# print(identity(5))

# 5.How can you use a lambda function to add 1 to an argument?

# add_one = lambda x: x + 1
# print(add_one(2))

# 6. How do you call a lambda function directly without assigning it to a variable?
# print((lambda x: x + 1)(4))

# 7. Can a lambda function have multiple arguments?
# show me the example also
# call lambda directly

# yes, list arguments separated by commas without perenthenses
# full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"
# print(full_name("pablo", "gaviria"))

# print((lambda first, last:f'Full name: {first.title()} {last.title()}')("pablo", "gaviria"))

# 8. Can a lambda function be named?
# Yes we can assign it to a variable

# 9. When should you use a lambda function?
# give me an example
# in a short tasks like map, filter, or soted

# names = ['Buido', "Aurelio", "Van"]
# sorted_names = sorted(names, key=lambda name: len(name))
# print(sorted_names)

# 10. What is an anonymous function in Python?
# anonymous function is a function wich don't have a name and its created with labmda keyword
# example
# what this function do ? lambda x, y: x + y

# 11. What is an Immediately Invoked Function Expression (IIFE)?
# IIFE is pattern where function defined and immediately called

# example
# print((lambda x, y: x + y)(2, 3))

# 12.What is a higher-order function in Python?
# higher order fuction is a function which takes one or more functions 
# as an arguments or returns a function, lambda fuctions often used in
#  higher-order functions in Python
# example

# high_ord_func = lambda x, func: x + func(x)

# print(high_ord_func(2, lambda x: x * x))
# print(high_ord_func(2, lambda x: x + 3))

# 13. What is the advantage of using lambda functions in Python?
# they allow one-line fuction definitions and it is useful for short 
# operations, like sorting

# 14. how can you spread single lambda expression in several lines?
# print((lambda x: x + 1)(8))

# print((lambda x:
#        (x + 1))(8))

# write the lambda function which returns 'odd' if number is odd

# write a lambda function which sums the dict values

# wtite lambda function which accepts one positional argument,
# two keywordonly arguments and return sum 

# 15. what map() function is used for?
# map function applies function  to each item in itarable like list or
# tuple and gives back new iterable with results.

# convert list of strings into list of integers using map
# lst = ['1', '2', '3']

# double each element of a list with map function
# nums = [1, 2, 3, 4]

# double each list item using lambda and map()
# nums = [1, 2, 3, 4]

# add 2 itarables each elements using lambda and map()
# a = [1, 2, 3]
# b = [3, 4, 5]

# convert list of strings to uppercase
# fruits = ['apple', 'banana', 'orange']

# extract the firs character from each string in a list using lambda and map()
# words = ['apple', 'banana', 'cherry']

# remove leading and trailing whitespaces from each string in
# a list
# s = ['   hello  ', '  world  ']

# 16. Write a decorator that prints the name of the function being 
# called and test it with a simple function.

# Create a function that performs a simple operation (e.g., adds 
# 2 to a number) and apply a decorator to it.

# Use a decorator with a lambda function and call it with 
# an argument.

# Write lambda function that doubles numbers in range(3), apply
# the map() function, then create decorator that prints the name
# of the function being called, then apply the decorator to the
# lambda funcion and use map() again.

# Write a script to compare the outputs when decorating a regular 
# function versus a lambda function.

# What is a decorator in Python?
# decorator is function which decorates the original function

# How do you use a decorator with a lambda function?
# we are directly passing lambda function to a decorator

# 17. closure example:
# write a function that accepts paremeter x, defines a variable 
# y=4, defines a inner functiion that: prints the values of 
# x, y and z and returns the sum of x, y and z
# use for loop, call outer function in range(3), assign returned
# function to a variable closure, call closure(i+5) and print
# the result

# what will be output of this function?
# def outer_func(x):
#     y = 4
#     return lambda z: x+y+z

# for i in range(3):
#     closure = outer_func(i)
#     print(f"closure({i+5}) = {closure(i+5)}")

# 18.
# def wrap(n):
#     def f():
#         print(n)
#     return f

# numbers = 'one', 'two', 'three'
# funcs = []

# for n in numbers:
#     funcs.append(wrap(n))
    
# for f in funcs:
#     f()
# Evaluation time 
def warp(n):
    def f():
        print(n)
    return f

numbers = 'one', 'two', 'three'
funcs = []

for n in numbers:
    funcs.append(lambda: print(n))

for f in funcs:
    f()
