
# Operations in a list
# add [c, d, e] at the and of ["a", "b"], OUTPUT ["a", "b",["c", "d", "e"]]
# lst = ["a", "b"]
# lst.append(["c", "d", "e"])

# Task 6
# add [c d e] at the end of ["a", "b"],OUTPUT ["a","b","c","d","e",]
# letters = ["a", "b"]
# letters.extend(["c", "d", "e"])
# print(letters)

# Task 7
#add "b" between ["a", "c"],OUTPUT a = ["a","b", "c"]
# letters = ["a", "c"]
# letters.insert(1,"b")
# print(letters)
# -------------------------------------------------continue from here--------------------------------------------------------
# Task 8
# remove first b from ["a","b", "c", "d", "e","b"]
# letters = ["a","b", "c", "d", "e","b"]
# letters.remove("b")
# print(letters)

# Task 9
# remove last character from chars = ["a","b", "c", "d", "e"] and also print
# removed character
# letters = ["a","b", "c", "d", "e"]
# print(letters.pop())
# print(letters)

# Task 10
# remove b, e, c and d from chars = ["a","b", "c", "d", "e"] and also print removed
# character
# letters = ["a","b", "c", "d", "e"]
# print(letters.pop(1))
# print(letters)
# print(letters.pop())
# print(letters)
# print(letters.pop(-2))
# print(letters)
# print(letters.pop())
# print(letters)

# Task 11
# check if "qux", "py" and "thud" are in words = ["foo", "bar", "baz", "qux", "quux", "corge"]
# words = ["foo", "bar", "baz", "qux", "quux", "corge"]
# print("qux" in words)
# print("py" in words)
# print("thud" not in words)

# Task 12
# add words = ["foo", "bar", "baz", "qux", "quux", "corge"] bear and wolf and multiple words 2 times
# words = ["foo", "bar", "baz", "qux", "quux", "corge"]
# print(words + ["bear", "wolf"])
# print(words * 2)

# Task 13
# numbers = [2, 7, 5, 4, 8] calculate length of list,take minimum number from list,take max number from list, sum all numbers in list
# print(len(numbers))
# print(min(numbers)) 
# print(max(numbers)) 
# print(sum(numbers))

# Task 14
# swap foo,bar to bar,foo. do it with unpucking also a = "foo" b = "bar"
# temp = a
# a = b
# b = temp 
# print(a,b)

# a = "foo" b = "bar"
# a, b = b, a
# print(a ,b)

# Task 15 ----------------------------
# take TWINS and ROCKIES values from 
# team = {
#     'Colorado'  : 'Rockies',
#     'Boston'    : 'Red Sox',
#     'Minnesota' : 'Twins',
#     'Milwaukee' : 'Brewers',
#     'Seattle'   : 'Mariners'
# }
# print(team["Minnesota"])
# print(team["Colorado"])

# Task 16
# add "Kansas" : "Royals" to the dict"
# team["Kansas"] = "Royals"
# print(team)

# Task 17
# update value of Seattle to Seahawks and then delete Seattle
# team["Seattle"] = "Seahawks"
# print(team)
# del team["Seattle"]
# print(team)
# --------------------------
# Task 18
# take a and c from d = {5 : "a", 1 : "b", 4 : "c", 3 : "d"}
# print(d[5])
# print(d[4])

# Task 19 
# create a empty dictionary of person with keys fname,lname,age,spouse,children,pets
# person = {}
# person["fname"] = "David"
# person["lname"] = "Naveriani"
# person["age"] = 30
# person["spouse"] = "Anna"
# person["children"] = ["Gio", "Keti"]
# person["pets"] = {"dog": "baksi", "cat" : "hashi"}
# print(person)

# Task 20
# whats the name,age and children of person?
# print(person["fname"])
# print(person["age"])
# print(person["children"])

# Task 21
# whats the name of last child and cats name
# print(person["children"][-1])
# print(person["pets"]["cat"])
# ---------------------------------------------------
# Task 22
#take aaa, bbb and ccc from foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
# print(foo[42])
# print(foo[2.78])
# print(foo[True])

# Task 23
# take 2 and 3 from d = {int: 1, float : 2, oct: 3}
# d = {int: 1, float : 2, oct: 3}
# print(d[float])
# print(d[oct])

# Task 24
# take a and c from d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
# print(d[(1,1)])
# print(d[(2, 1)])

# Task 25
# clear all items in d = {'a': 10, 'b': 20, 'c': 30}
# d = {'a': 10, 'b': 20, 'c': 30}
# d.clear()
# print(d)

# Task 26
# get the value of b and z with get method from d = {'a': 10, 'b': 20, 'c': 30}
# d = {'a': 10, 'b': 20, 'c': 30}
# print(d.get("b"))
# print(d.get("z"))

# Task 27
# take all items in d = {'a': 10, 'b': 20, 'c': 30},than take b and 20
# d = {'a': 10, 'b': 20, 'c': 30}
# print(list(d.items()))
# print(list(d.items())[1][0])
# print(list(d.items())[1][1])

# Task 28
# take keys from d = {'a': 10, 'b': 20, 'c': 30} with key method
# print(list(d.keys()))

# Task 29
# take values from d = {'a': 10, 'b': 20, 'c': 30} with method values
# print(list(d.values()))

# Task 30
# remove b : 20 from d = {'a': 10, 'b': 20, 'c': 30}
# print(d.pop("b"))
# print(d)

# Task 31
# remove c:30 from d = {'a': 10, 'b': 20, 'c': 30}
# d = {'a': 10, 'b': 20, 'c': 30}
# print(d.popitem())
# print(d)

# Task 33
# megre 2 dictionaries d1 = {'a': 10, 'b': 20, 'c': 30} and d2 = {'b': 200, 'd': 400}
# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'b': 200, 'd': 400}
# d1.update(d2)
# print(d1)

# Task 34
# update d1 = {'a': 10, 'b': 20, 'c': 30} to 
# {'a': 10, 'b': 200, 'c': 30, 'd': 400} with list of tuples
# d1 = {'a': 10, 'b': 20, 'c': 30}
# d1.update([("b", 200),("d", 400)])
# print(d1)

# Task 35
# update d1 = {'a': 10, 'b': 20, 'c': 30} to 
# {'a': 10, 'b': 200, 'c': 30, 'd': 400} with list of keyword arguments
# d1 = {'a': 10, 'b': 200, 'c': 30, 'd': 400}
# d1.update(b = 200, d = 400)
# print(d1)

#FUNCTIONS
# Task 36
# make function f with arguments qty,item,price and print
# 6 bananas cost $1.75
# def f(qty, item, price):
#     print(f'{qty} {item} cost ${price}')

# f(qty = 6, item = "bananas", price = 1.75)


#Task 37 
# make function f with default parameters qty=6, item='bananas,price=1.74
# OUTPUTS should be : 
# 4 apples cost $2.24
# 4 apples cost $1.74
# 4 bananas cost $1.74
# 6 bananas cost $1.74
# 9 kumquats cost $1.74
# 6 bananas cost $2.29
# def f(qty = 6, item ="bananas", price = 1.74):
#     print(f"{qty} {item} costs ${price}")
# f(qty = 4, item = "apples", price = 2.24)
# f(qty = 4, item = "apples")
# f(qty = 4)
# f()
# f(qty = 9, item = "kumquats")
# f(qty = 6, price = 2.29)

# Task 38
# create function f and give argument my_list[] which will be empty array, append to list ###
# print ['foo', 'bar', 'baz', '###']
# print [1, 2, 3, 4, 5, '###']
# def f(my_list = []):
#     my_list.append("###")
#     print(my_list)
# f(["foo", "bar", "baz"])
# f([1,2,3,4,5])

# Task 39
# Write a function f(x) that assigns "foo" to x. Iterate over different data types (integer, dictionary, set, string, and list) 
# using a for loop, passing each element to f(x). After each call to f(x), print the element to observe if it was modified.
# def f(x):
#     x = "foo"
# for i in(
#     40,
#     dict(foo = 1, bar = 2),
#     {1,2,3},
#     "bar",
#     [1,2,3]):
#     f(i)
#     print(i)

# Task 40
# Define a function f(x) that modifies the first element of a list x to "---". Create a list my_list with several strings, 
# then call f(my_list) and see if the first element was changed.
# def f(x):
#     x[0] = "---"
# my_list = ["foo", "bar", "baz"]
# f(my_list)
# print(my_list)

# Task 41
# Define a function f(x) that changes the value of the "bar" key in a dictionary x to 22. 
# Create a dictionary my_dict with several key-value pairs, call f(my_dict), and print my_dict to check if the "bar" key was updated.
# def f(x):
#     x["bar"] = 22
# my_dict = {"foo" : 1, "bar" : 2, "baz" : 3}
# f(my_dict)
# print(my_dict)

# Task 42
# Define a function f(x). If x is less than 0 or greater than 100,the function should return without doing anything. 
# Otherwise, it should print x.Test the function by calling f with -3, 105, and 64 and observe the output.
# def f(x):
#     if x < 0:
#         return
#     if x > 100:
#         return
#     print(x)

# f(-3)
# f(105)
# f(64)

# Task 43
# Create a function greet(name) that checks if the input name is empty. If it is,return the message "Name cannot be empty."
# Otherwise, return a greeting message.Test the function by printing the output for a valid name and an empty string.
# def greet(name):
#     if name == "":
#         print("Name can not be empty.")
#     else:
#         print(f"Hello! {name}")
# greet("Zviad")
# greet("")

# Task 44
#Define a function f() that returns a dictionary with keys "foo", "bar", and "baz" associated with the values 1, 2, and 3. 
# Print the entire dictionary, print the value associated with the key "baz".
# def f():
#     return dict(foo = 1, bar = 2, baz = 3)
# print(f())
# print(f()["baz"])

# Task 45
#Create a function f() that returns the string "foobar".Print ob

# def f():
#     return "foobar"
# print(f()[2:4])

# Task 46
# Define a function f() that returns a list containing the strings ['foo', 'bar', 'baz', 'qux']. Print the  entire list,
# then print the baz, and finally print the list in reverse order.

# def f():
#     return ['foo', 'bar', 'baz', 'qux']
# print(f())
# print(f()[2])
# print(f()[::-1])

# Task 47
# Define a function f() that returns four strings:"foo", "bar", "baz", and "qux".Print the type of the value. Store the result of the 
# function in a variable t and print t.Unpack the returned values into four variables a, b, c, and d, then print these variables.

# def f():
#     return "foo", "bar", "baz", "qux"

# print(type(f()))
# t = f()
# print(t)
# a, b, c ,d = f()
# print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# Task 48
# Define two functions, f() and g(), where f() has a return statement with no value, and g() does nothing (use pass).check if calling 
# f() or g() results in a truthy value.

# def f():
#     return

# def g():
#     pass   

# if f() or g():
#     print("yes")
# else:
#     print("no")

# Task 49
# Define two versions of a function called double.In the first version, try doubling x,assign x to 10 then print x to see if 
# it changes. In the second version, use return x * 2 and print the result to observe the difference.

# def double(x):
#     x *= 2
# x = 10
# double(x)
# print(x)

# def double(x):
#     return x * 2
# x = 10
# print(double(x))

# Task 50
# Define a function double_list(x) that takes a list x and doubles each element in the list.go through each element with while loop, 
# doubling its value directly in the list. Create a list a with several numbers,call double_list(a), and print a to see the modified 
# values.
  
# def double_list(x):
#     i = 0
#     while i < len(x):
#         x[i] *= 2
#         i += 1

# a = [1, 2, 3, 4, 5]
# double_list(a)
# print(a)

# Task 51
# Modify the function double_list so that it multiplies each element in a list by 2.in function create an empty list, than append 
# elements there 

# def double_list(x):
#     r = []
#     for i in x:
#         r.append(i * 2)
#     return r

# a = [1,2,3,4,5]
# a = double_list(a)
# print(a)

# Task 52
# Write a  function that calculates the average of three numbers.

# def avg(a,b,c):
#     return (a+b+c) / 3
# print(avg(1,2,3))

# Task 53
# Write a function that calculates the average of up to five numbers, with optional parameters.test function with arguments: avg(5)
# avg(5,5), avg(1,2,3)
# def avg(a, b = 0, c = 0, d = 0, e = 0):
#     return (a + b + c + d + e) / 5

# print(avg(5))
# print(avg(5, 5))
# print(avg(1, 2, 3))

# Task 54
# Create function which calculates the avarage of list.Create a function avg that takes a single argument.Inside the function, 
# use a for loop to iterate through the list and calculate the sum of its elements.Divide the total sum by the length of the list to 
# get the average.check avarage of list 1,2,3 and 1,2,3,4,5 and tuple 1,2,3
# def avg(x):
#     total = 0
#     for i in x:
#         total += i
#     return total / len(x)

# print(avg([1, 2, 3]))
# print(avg([1, 2, 3, 4, 5]))
# print(avg((1, 2, 3, 4, 5)))

# Task 55
# Create a function called f that uses *args to accept a variable number of arguments.Inside the function: Print the args,
# Print the type of args and the number of arguments it contains.check 1,2,3 , foo,bar,baz , list 1,2,3 and string foo

# def f(*args):
#         print(args)
#         print(type(args))
#         for i in args:
#                 print(i)

# f(1, 2, 3)
# f("foo", "bar", "baz")
# f([1, 2, 3])
# f("foo")

# Task 56
# Create a function called avg that accepts a variable number of arguments using *args.Inside the function:Calculate the average by 
# summing all the arguments Divide the total by the number of arguments.

# def avg(*args):
#         return sum(args) / len(args)

# print(avg(1,2,3))
# print(avg(1,2,3,4,5))

# Task 57
# Create a function called f that takes three parameters: x, y, and z.Inside the function, use formatted strings to print 
# the values of x, y, and z with labels.Test the function by: Calling f(1, 2, 3).Creating a tuple t with the values 
# ("foo", "bar", "baz"). Calling the function f with the unpacked values of  the tuple t.do same to list and set

# def f(x,y,z):
#     print(f"x = {x}")
#     print(f"y = {y}")
#     print(f"z = {z}")

# f(1,2,3)
# t = ("foo","bar","baz")
# f(*t)
# a = ["foo", "bar", "baz"]
# print(type(a))
# f(*a)
# s = {1,2,3}
# print(type(s))
# f(*s)

# Task 58
# Create a function called f that uses **kwargs. Inside the function:Print the kwargs dictionary. Print the type of kwargs.
# Use a for loop to iterate through each key-value  pair in kwargs and print them in the format:key -> value.
# Test the function by calling f with three keyword arguments: foo=1, bar=2, and baz=3.

# def f(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key, val in kwargs.items():
#         print(key, "->", val)

# f(foo=1,bar=2,baz=3)

# Task 59
# Create a function called f(a,b,c).Inside the function, use formatted strings to print the values of a, b, and c with labels.
# Create a dictionary d with the keys "a", "b", and "c" containing appropriate values, Call the function.

# def f(a,b,c):
#     print(f"a = {a}")
#     print(f"b = {b}")
#     print(f"c = {c}")
# d = {"a":"foo", "b" : 25, "c": "bar"}
# f(**d)

# Task 60
# Create a function called f that takes two parameters a and b, followed by *args  and **kwargs Inside the function, print the values 
# of a and b,args and kwargs.Test the function

# def f(a, b, *args, **kwargs):
#     print(f"a = {a}")
#     print(f"b = {b}")
#     print(f"args = {args}")
#     print(f"kwargs = {kwargs}")

# f(1, 2,"foo", "bar", "baz", x=100, y=200, z=300)

# Task 61
# Create a function called f that uses *args. Inside the function, use a for loop to iterate through args and print each argument.
# Create a list a containing the elements [1, 2, 3].Create a tuple t containing the elements (4, 5, 6).Create a set s containing the 
# elements {7, 8, 9}.Call the function f using the unpacking syntax with all three data structures

# def f(*args):
#     for i in args:
#         print(i)

# l = [1, 2, 3]
# t = (4, 5, 6)
# s = {7, 8, 9}

# f(*l, *t, *s)

# Task 62
# Create a function called f that uses **kwargs. Inside the function, use a for loop to iterate through kwargs items and print each key
# and its corresponding value.Create two dictionaries:d1 with keys "a" and "b" having values 1 and 2.d2 with keys "x" and "y" having 
# values 3 and 4. Call the function f using the unpacking syntax with 

# def f(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "->", v)
    
# d1 = {"a" : 1, "b" : 2}
# d2 = {"x" : 3, "y" : 4}

# f(**d1, **d2)

# Task 63
# Create a function called f that uses *args.Inside the function, use a for loop to iterate through  args and print each argument.
# Call the function  using two lists:[1, 2, 3]. [4, 5, 6].Use the unpacking syntax to pass both lists to the function

# def f(*args):
#     for i in args:
#         print(i)

# f(*[1,2,3], *[4,5,6])

# Task 64
# Create a function called concat that uses *args. Inside the function, use the join() method to concatenate the strings in args, 
# separating them  with a period (.).Print the concatenated result.test ("a", "b", "c"), ("foo", "bar", "baz")

# def concat(*args):
#     print(f"-> {'.'.join(args)}")

# concat("a", "b", "c")
# concat("foo", "bar", "baz")

# Task 65
# Create a function called concat that takes a string prefix and  *args.Inside the function, use the join() method to 
# concatenate the strings in args, separating them with a period (.), and prepend the prefix.Test the function by calling:
# concat("//", "a", "b", "c").concat("... ", "foo", "bar", "baz").

# def concat(prefix, *args):
#     print(f"{prefix}{".".join(args)}")

# concat("//", "a", "b", "c")
# concat("... ", "foo", "bar", "baz", "qux")

# Task 66
# Create a function called concat that takes *args and an optional parameter prefix with a default value of "-> ".
# Inside the function, use the join() method to concatenate the strings in args, separating them with a period (.), and prepend the 
# prefix.Print the result.Test the function by calling:concat("a", "b", "c", prefix="... "),("a", "b", "c").

# def concat(*args, prefix="-> "):
#     print(f"{prefix}{".".join(args)}")

# concat("a", "b", "c")
# concat("a", "b", "c", prefix="... ")

# Task 67
# Create a function called concat  *args, an optional parameter prefix with a default value of "-> ", and another optional parameter 
# sep with a default value  of ".". Inside the function, use the join() method to concatenate the strings in args, separating them 
# with sep, and prepend the prefix.print the result,Test the function by calling:("a", "b", "c"), ("a", "b", "c", prefix="// "), 
# ("a", "b", "c", prefix="// ", sep="-").

# def concat(*args,prefix="-> ",sep="."):
#     print(f"{prefix}{sep.join(args)}")

# concat("a", "b", "c")
# concat("a", "b", "c", prefix="// ")
# concat("a", "b", "c", prefix="// ", sep="-")

# Task 68 
# Create a function called oper that takes two parameters x and y, and an optional parameter op with  a default value of "+".
# Inside the function, use conditional statements to check the value of op: If op is "+", return the sum of x and y.
# If op is "-", return the difference of x and y. If op is "/", return the result of dividing x by y. For any other operator, return None.
# Test the function by calling: (oper(3, 4)).(oper(3, 4, "+")).(oper(3, 4, "/")).

# def op(x, y, op="+"):
#     if op == "+":
#         return x + y
#     elif op == "-":
#         return x - y
#     elif op == "/":
#         return x / y
#     else:
#         return None

# print(op(3, 4))
# print(op(3, 4, "+"))
# print(op(3, 4, "/"))

# Task 69
# create function oper(x, y, *ignore, op="+"),check op and do appropriate operations,check + - /,otherwise return none
# check (3, 4, op="+"), (3, 4, "i do not care"),(3, 4,"i dont care", op="/"),(3, 4, "/") 

# def oper(x, y, *ignore, op="+"):
#     if op == "+":
#         return x + y
#     elif op == "-":
#         return x - y
#     elif op == "/":
#         return x / y
#     else:
#         return None
    
# print(oper(3, 4, op="+"))
# print(oper(3, 4, "i dont care"))
# print(oper(3, 4, "dont care", op="/"))
# print(oper(3, 4, "/"))

# Task 70
# # Create function f(x, y, /, z),Print values of x, y, and z.x and y should only be passed positionally, z can be passed by name
# Test cases: f(1, 2, 3),f(1, 2, z=3),f(x=1, y=2, z=3)  # should raise an error

# def f(x, y, /, z):
#     print(f"x : {x}")
#     print(f"y : {y}")
#     print(f"z : {z}")

# f(1, 2, 3)
# f(1, 2, z=3)
# f(x=1, y=2,z=2)

# Task 71
# # Create function f(x, y, /, z, w, *, a, b),Print values of x, y, z, w, a, and b. x and y are positional-only, z and w can be 
# positional  or keyword, a and b must be keyword-only.Test cases: f(1, 2, z=3, w=4, a=5, b=6), f(1, 2, 3, w=4, a=5, b=6)
# f(1, 2, 3, w=4, a=5, 6)  # should raise an error

# def f(x, y, /, z, w, *, a, b):
#     print(x, y, z, w, a, b)

# f(1,2,z=3,w=4,a=5,b=6)
# f(1,2,3,w=4,a=5,b=6)
# f(1,2,3,w=4,a=5,6)

# Task 72
# Create function avg(*args) Include a docstring: "Returns the average" Calculate and return the average of all 
# numeric values  in args

# def avg(*args):
#     """ 
#         Returns the avarage
#     """
#     return sum(args) / len(args)

# print(avg(1,2,3))

# Task 73
# # Create function f(a: '<a>', b: '<b>') -> '<ret_value>' than pass 
# Print f.__annotations__ to see all annotations, Print specific annotations for "a", "b", and "return")

# def f(a: '<a>', b: '<b>') -> '<ret_value>':
#     pass

# print(f.__annotations__)
# print(f.__annotations__["a"])
# print(f.__annotations__["b"])
# print(f.__annotations__["return"])

# Task 74
# Create function with annotations int, str and return value float Print a and b, then return 3.5
# Test cases:(1, "foo")), print(f.__annotations__) 

# def f(a: int, b: str) -> float:
#         print(a, b)
#         return(3.5)

# print(f(1, "foo"))
# print(f.__annotations__)

# >>>>>>>>>>>>>>>>>>>>>> NAMESPACES <<<<<<<<<<<<<<<<<<<<<<<
# Task 75
# Create a function called f() that prints "start f()". Inside f(), define another function called g() that prints "start g()" and 
# "End g()", then returns to f().Call g() inside f() so that it runs when f() is executed. After g() finishes, f() should print 
# "End f()".

# def f():
#     print("Start f()")

#     def g():
#         print("Start g()")
#         print("End g()")
#         return
#     g()

#     print("End f()")
#     return 

# f()

# Task 76
# Define a variable x with the value 'global' outside. Then, create a function f() that contains another function g(). 
# In g(), add a print(x) statement.

# x = "global"
# def f():

#     def g():
#         print(x)
#     g()

# f()

# Task 77
# Define a variable x with the value 'global' outside. Then, create a function f() where x is redefined as 'enclosing'. 
# Inside f(), define another function g() that prints x.

# x = "global"
# def f():
#     x = "enclosing"

#     def g():
#         print(x)
#     g()

# f()

# Task 78
# Define a variable x with the value 'global' outside. In a function f(), redefine x as 'enclosing'.
# Inside f(), define another function g() where x is redefined again as 'local' and then printed.

# x = "global"
# def f():
#     x = "enclosing"

#     def g():
#         x = "local"
#         print(x)
#     g()
# f()


# Task 79
# Define a global variable x and assign it the value 'foo'.print globals.access this variable directly by referring to x, or indirectly 
# through the globals() dictionary.Verify that x and globals()['x'] are the same object by using the is operator.

# x = "foo"
# print(globals())
# print(x)
# print(globals()["x"])
# print(x is globals()["x"])

# Task 80
# Create a function f(x, y) that takes two parameters. Inside f(),define a variable s with the value 'foo', then print the dictionary 
# returned by locals().test f(1, 2)

# def f(x, y):
#     s = "foo"
#     print(locals())

# f(1, 2)

# Task 81 
# Assign the result of globals() to a variable g. print g,Then,define new variables x and y with values 'foo' and 
# 29,respectively.print g again to see difference

# g = globals()
# print(g)
# x = "foo"
# y = 29
# print(g)

# Task 82
# Create a function f() that defines a local variable s with the value 'foo'. Inside the function, use locals() 
# to create a variable loc that holds a copy of the local namespace, then print loc. After define another local 
# variable x with the value 20, and print loc again. Then, try to modify 
# the value of s in loc and print s to see if it changes.

# def f():
#     s = "foo"
#     loc = locals()
#     print(loc)

#     x = 20
#     print(loc)

#     loc["s"] = "bar"
#     print(s)

# f()

# Task 83
# Define a global variable x with the value 20. Then,create a function f() that assigns x the value 40 and 
# prints x. check the value of the global x to  see if it has changed.

# x = 20
# def f():
#     x = 40
#     print(x)
# f()
# print(x)

# Task 84
# Define a global variable my_list as a list ['foo', 'bar', 'baz']. Create a function that 
# modifies the second element of my_list to 'quux'. check the contents of my_list to see 
# the modification. Next,create another function f() that attempts to reassign my_list to ['qux', 'quux'].
# Call this new f() and check my_list again.

# my_list = ["foo", "bar", "baz"]

# def f():
#     my_list[1] = "quux"

# f()
# print(my_list)

# def f():
#     my_list = ["qux", "quux"]

# f()
# print(my_list)

# Task 85
# Define a global variable x with the value 20. Create a function f() that uses the global declaration for x, 
# assigns x the value 40, and then prints x. check the value of x to confirm that it has been modified in the 
# global scope.

# x = 20
# def f():
#     global x
#     x = 40
#     print(x)

# f()
# print(x)

# Task 86
# do this task as task 85, but this time change x value as globals()

# x = 20
# def f():
#     globals()["x"] = 40
#     print(x)

# f()
# print(x)

# Task 87
# Define a function f() that sets x to 20. Inside f(),define a nested function g() that sets x to 40,print x, 
# then call g() and print x  within f(). observe the value of x in the enclosing scope to see if it was modified.

# def f():
#     x = 20

#     def g():
#         x = 40
#         print(x)
#     g()
#     print(x)
# f()

# Task 88
# Create a function named f() that sets a variable x to 20.Inside f(), define another function g() that tries to 
# change x to 40 using the global keyword. Call g() within f() and then print x in f().Run f() and observe the 
# output.

# def f():
#     x = 20

#     def g():
#         global x
#         x = 40
        
#     g()
#     print(x)
# f()

# Task 89
# Define a function f() that assigns 20 to a variable x. Inside f(), create a nested function g() that attempts 
# to set x to 40 using the global keyword. Call g() within f() and print the value.After running f(), print x 
# again outside the function.You’ll observe that x in f() remains 20, but x in the global scope becomes 40 because
#  the global keyword creates or modifies a variable in the global scope, not in the function’s enclosing scope.

# def f():
#     x = 20

#     def g():
#         global x
#         x = 40
#     g()
#     print(x)
# f()
# print(x)

# Task 90
# Define a function f() that sets a variable x to 20. Inside f(), define another function g() that uses the 
# nonlocal  keyword to modify x and set it to 40. Call g() within f()  and print the value of x.

# def f():
#     x = 20
    
#     def g():
#         nonlocal x
#         x = 40
#         g()
#     print(x)
# f()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>> Python Modules and Packages: An Introduction <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Task 91 
# make mod.py file and write this code:
# s = "If Comrade Napoleon says it, it must be right."
# a = [100, 200, 300]
# def foo(arg):
#     print(f'arg = {arg}')
# import mod.py file and print all elements
# import mod
# print(mod.s)
# print(mod.a)
# mod.foo(["alpha", "beta"])

# Task 91 
# check sys path and the location of mod file
# import mod
# import sys
# print(sys.path)
# print(mod.__file__)
# import mod
# import sys

# print(sys.path)
# print(mod.__file__)

# Task 92
# from mod import s and foo and print them
# from mod import s, foo
# print(s)
# foo("quux")

# Task 93
# make a list a = ["foo", "bar", "baz"] and print list,than
# import a from mod and print a again.
# a = ["foo", "bar", "baz"]
# print(a)
# from mod import a
# print(a)

# Task 94
# from mod import all objects and print them all
# from mod import *
# print(s)
# print(a)
# print(foo)

# Task 95
# make s = "foo",a = ["foo", "bar", "baz"],than import s as string and a as alist print them all
# s = "foo"
# a = ["foo", "bar", "baz"]
# from mod import s as kring, a as alist
# print(s)
# print(kring)
# print(a)
# print(alist)

# Task 96
# import whole module as my_module, than print them all
# import mod as my_module
# print(my_module.a)
# print(my_module.s)
# my_module.foo("qux")

# Task 97
# Define a function bar() that imports another function foo() from mod , Inside bar(), call foo() with an argument
#  "corge" and  execute it.
# def bar():
#     from mod import foo
#     foo("courge")

# bar()

# Task 98
# Run dir() in an empty environment to see the default objects present.Import  mod and then run dir() again to observe the addition of 
# mod to the namespace.Access mod.s to verify it contains a specific string,Call mod.foo() with a list [1, 2, 3].import a and then 
# run dir().Confirm that a holds [100, 200, 300].Import s from mod as string,then check dir() to see string added to the namespace.
# Finally, verify that string holds the value.

# print(dir())
# import mod 
# print(dir())
# print(mod.s)
# print(mod.foo([1, 2, 3]))
# from mod import a
# print(dir())
# print(a)
# from mod import s as string
# print(dir())
# print(string)

# Task 99
# generate mod file as it prints everything inside and than execute it from terminal, than execute it with import
# s = "If Comrade Napoleon says it, it must be right."
# in mod.py
# print(s)
# print(a)
# foo("quux")
# x = Foo()
# print(x)
# import mod


# Task 100
# modify mod file like above, than run it, than run it with import, it executes from terminal and not from import, because
# when u are executing __name__ = "__main__", and when u are importing __name__ = mod.
# s = "If Comrade Napoleon says it, it must be right."
# a = [100, 200, 300]
# def foo(arg):
#     print(f"arg = {arg}")
# class Foo:
#     pass
# if(__name__ == "__main__"):
#     print("Executing as standalone script")
#     print(s)
#     print(a)
#     foo("quux")
#     x = Foo()
#     print(x)
# import mod

# Task 101
# add the code to a fact.py file, Define a function fact(n) that calculates the factorial of n recursively. Use a one-line return 
# statement where fact(n) returns 1 if n is 1, otherwise it returns n * fact(n-1).Add a main check if (__name__ == '__main__') to 
# allow the script to be run directly. Within this block, import the sys module. If there’s at least one command-line 
# argument, call fact() with the integer value of the first argument (sys.argv[1]) and print the result.Running this program from the 
# command line with a number as an argument (e.g., python script.py 5) will print the factorial of that number. This setup 
# demonstrates both recursion and handling command-line arguments in Python.

# def fact(n):
#     return 1 if n == 1 else n * fact(n - 1)

# if (__name__ == "__main__"):
#     import sys
#     if len(sys.argv) > 1:
#         print(fact(int(sys.argv[1])))

# THAN import fact function from fact.py and print factorial of 6
# from fact import fact   
# print(fact(6))

# Task 102
# add in mod:
# a = [100, 200, 300]
#print("a =", a)

# than import mod 3 times, than print [100, 200, 300]
# import mod
# import mod
# import mod
# print(mod.a)

# Task 103
# first import the module normally and execute it, then use importlib.reload() to re-run it without restarting the interpreter.
# import mod 

# import importlib
# importlib.reload(mod)


# Task 104
# make modules mod1 and mod2 and put them in pkg folder:
#mod 1
# def foo():
#     print("[mod1] foo()")

# class Foo:
#     pass

#mod 2
# def bar():
#     print("[mod2] bar")

# class Bar:
#     pass


# Task 105
# First, import both modules.Call foo() from mod1 and create an instance of Bar from mod2. Print the instance to see the result.
# Next, import foo from mod1 directly and call it.Finally, import Bar from mod2 with an alias Qux, then create an instance of 
# Qux and print it.

# import pkg.mod1, pkg.mod2
# pkg.mod1.foo()
# x = pkg.mod2.Bar()
# print(x)
# from pkg.mod1 import foo
# foo()
# from pkg.mod2 import Bar as Qux
# x = Qux()
# print(x)

# Task 106
# First, import mod1 directly from the package and call foo().Next, import mod2 from pkg with an alias quux, then call bar().Finally, 
# import the entire package. This allows you to reference pkg as a module.

# from pkg import mod1
# mod1.foo()
# from pkg import mod2 as qux
# qux.bar()
# import pkg
# print(pkg)

# Task 107
# add __init.py__ in pkg, in __init.py__ add code below
# ---
# print(f'Invoking __init__.py for {__name__}')
# A = ['quux', 'corge', 'grault']
# ---

# In mod1.py, define a function foo that imports and prints A.Import the pkg, which will initialize A and invoke __init__.py. 
# Import mod1 from pkg and call foo(), which will access and print the global variable A.

# import pkg
# print(pkg.A)
# from pkg import mod1
# mod1.foo()

# Task 108 
# In __init__.py remove A (also in mod1) and import packages. This will trigger the __init__.py file, which will automatically 
# import mod1 and mod2. Call foo() from mod1 and bar() from mod2.

# import pkg
# pkg.mod1.foo()
# pkg.mod2.bar()

# Task 109
# ADD in mod3:
# def baz():
#     print('[mod3] baz()')

# class Baz:
#     pass
# ADD in mod4:
# def qux():
#     print('[mod4] qux()')

# class Qux:
#     pass

#  see names in local scope, than import from mod3 everything and again
# see local names.than call baz function and print Baz

# print(dir())
# from pkg.mod3 import *
# print(dir())
# baz()
# print(Baz)

# Task 110
# output local names, than import everything from package,again print local names, than again see local names. ADD list of all modules 
# in init.py, call bar from mod2 and print Qux from mod4
# print(dir())
# from pkg import *
# print(dir())
# print(dir())
# from pkg import *
# print(dir())
# mod2.bar()
# print(mod4.Qux)


# Task 111
# in mod1 define foo in __all__, than output namespaces,import everything from mod1, than again display namespaces, call function foo 
# and Foo # erro should arise

# print(dir())
# from pkg.mod1 import *
# print(dir())
# foo()
# print(Foo)

# Task 112
# move mod1 and mod2 in sub_pkg1 and others in sub_pkg2 folder, import mod1 and call the function foo. import mod2 and
# call the function bar. import baz and run it.import qux as grault and run it.

# import pkg.sub_pkg1.mod1
# pkg.sub_pkg1.mod1.foo()
# from pkg.sub_pkg1 import mod2
# mod2.bar()
# from pkg.sub_pkg2.mod3 import baz
# baz()
# from pkg.sub_pkg2.mod4 import qux as grault
# grault()

# Task 113
# in mod3 file import function foo and call it,than import
# mod3 and call function foo

# IN mod3 file:
# from pkg.sub_pkg1.mod1 import foo
# foo()
# -----------
# from pkg.sub_pkg2 import mod3
# mod3.foo()

# CODEWAR 1
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Strings and Character Data in Python >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Task 114 
# print a,b with tab,newline, and rightwards arrow and

# print("a\tb")
# print("a\nb")
# print("\N{rightwards arrow}")


# Task 115
# concatenate strings with + greeting = "Hello", name = "Pythonista", OUTPUT Hello, Pythonista!!!
# print(greeting + ", " + name + "!!!")

# Task 116
# concatenate file = "app" as OUTPUT app.py
# file = "app"
# file += ".py"
# print(file)

# Task 117
# print " Hi" 10 times, than 0 and -1 times
# print("Hi " * 10)
# print("Hi " * 0)
# print("Hi " * -1)

# Task 118
# check if food is in sentences: "That food is delicious" ,"thats right" and check z if not sentences: "abc" and "xuz"

# print("food" in "That food is delicious")
# print("food" in "thats right")
# print("z" not in "abc")
# print("z" not in "xyz")

# Task 119
# calculate length of "Python", "", " ", than print snake and calculate length of snake

# print(len("python"))
# print(len(""))
# print("\N{snake}")
# print(len("\N{snake}"))

# Task 120
# convert to string 42, 3.14, [1, 2, 3], {"one": 1, "two": 2, "three": 3}
# {"A", "B", "C"}
# print(str(42))
# print(str(3.14))
# print(str([1, 2, 3]))
# print(str({"one": 1, "two": 2, "three": 3}))
# print(str({"A", "B", "C"}))

# Task 121
# print ascii number of a, # , print characters of 97,35,8364
# print(ord("a"))
# print(ord("#"))
# print(chr(97))
# print(chr(35))
# print(chr(8364))

# Task 122
# Create a string s with the value "foobar".
# extratc "oob" with negative indexing
# extract oob with positive indexing
# exctract foa
# exctract obr
# Create a second string numbers by repeating "12345" five times.
# exctratc 11111
# exctratc 55555
# exctract raboo
# exctract rbo
# exctract rf
# 55555 in reverse order

# s = "foobar"
# print(s[-5:-2])
# print(s[1:4])
# print(s[0:6:2])
# print(s[1:6:2])
# numbers = "12345" * 5
# print(numbers)
# print(numbers[::5])
# print(numbers[4::5])
# print(s[5:0:-1])
# print(s[5:0:-2])
# print(s[::-5])
# print(numbers[::-5])

# Task 123
# make variables debit = 300.00 credit = 450.00, make template of account report, than format template and calculate balance

# debit = 300.00
# credit = 450.00

# template = """
#         Account Report
#         Credit: ${credit:.2f}
#         Debit:  ${debit:.2f}
#         --------------------
#         Balance: ${balance:.2f}
# """
# print(template.format(
#         credit = credit,
#         debit = debit,
#         balance = credit - debit,

# ))

# Task 124
# do same task with % modulo operator

# debit = 300.00
# credit = 450.00

# template = """
#         Account Report
#         Credit: $%(credit).2f
#         Debit:  $%(debit).2f
#         --------------------
#         Balance: $%(balance).2f
# """

# print(template
#     % {
#         "credit":credit,
#         "debit":debit,
#         "balance": credit - debit
#     }
# )

# Task 125
# capitalize first world in "foo BaR 123 BAZ quX"
# lower all words in "FOO Bar 123 baz quX"
# change all letters case in "FOO Bar 123 baz quX"
# capitalize all first words in "the sun also rises"
# and here "what's happened to ted's IBM stock?"
# upper all words in "FOO Bar 123 baz qUx"

# print("foo BaR 123 BAZ quX".capitalize())
# print("FOO Bar 123 baz quX".lower())
# print("FOO Bar 123 baz quX".swapcase())
# print("the sun also rises".title())
# print("what's happened to red's IBM stock".title())
# print("FOO Bar 123 baz qUx".upper())

# Task 126 
# count "oo" in "foo goo moo"
# count "oo" in "foo goo moo" from 0 to 8
# find "foo" in "foo bar foo baz foo qux" from 4
# find foo in "foo bar foo baz foo qux" from 4 to 7
# find in which index is "foo" and than "grault" in "foo bar foo baz foo qux"
# recursively find "foo" in "foo bar foo baz foo qux"
# recursively find "foo"  in "foo bar foo baz foo qux" from 0 to 14, than from 10 to 14
# recursively find index of "foo" and than "grault" in "foo bar foo baz foo qux"
# check "foobar" if starts with "foo"
# check "foobar" if starts with bar from 3, than from 3 to 5
# check if "foobar" ends with "bar"
# check if "foobar" ends with "oob" from 0 to 4, than from 2 to 4
# check if "abc123", abc$123 is alphanumeric
# check if "abcABC", "abc123", "abc ABC" is letters
# check "123", "123abc" is numbers

# print("foo goo moo".count("oo"))
# print("foo goo moo".count("oo", 0, 8))
# print("foo bar baz foo qux".find("foo"))
# print("foo bar baz foo qux".find("grault"))
# print("foo bar foo baz foo qux".find("foo", 4))
# print("foo bar foo baz qux".find("foo", 4, 7))
# print("foo bar foo baz foo qux".index("foo"))
# # print("foo bar foo baz foo qux".index("grault"))
# print("foo bar foo baz foo qux".rfind("foo"))
# print("foo bar foo baz foo qux".rfind("grault"))
# print("foo bar foo baz foo qux".rfind("foo", 0, 14))
# print("foo bar foo baz foo qux".rfind("foo", 10, 14))
# print("foo bar foo baz foo qux".rindex("foo"))
# # print("foo bar foo baz foo qux".rindex("grault"))
# print("foobar".startswith("foo"))
# print("foobar".startswith("bar"))
# print("foobar".startswith("bar", 3))
# print("foobar".startswith("bar", 3, 5))
# print("foobar".endswith("bar"))
# print("foobar".endswith("foo"))
# print("foobar".endswith("oob", 0, 4))
# print("foobar".endswith("oob", 2, 4))

# Task 127
# check if "and" is keyword
# check if "abc", "Abc" is lower
# check if "a\tb", "a b", "" is printable
# check if " \t \n", "    a   " is whitespace
# check if "This Is A Title", "This IS a TitlE", "Give Me The #@$ Ball" is title
# check "ABC", "ABC1$D" is in upper case

# from keyword import iskeyword
# print(iskeyword("and"))
# print("abc".islower())
# print("Abc".islower())
# print("a\tb".isprintable())
# print("a b".isprintable())
# print("".isprintable())
# print("a\nb".isprintable())
# print(" \t \n".isspace())
# print("     a     ".isspace())
# print("This Is A Title".istitle())
# print("This is a title".istitle())
# print("Give Me The #$#@ Ball!".istitle())
# print("ABC".isupper())
# print("ABC1$D".isupper())

# Task 128 
# center "foo" with width 20, than "bar" with 20,"-" 
# expand tabs "a\tb\tc","a\tb\tc"
# expand tabs in "a\tb\tc" with size 4
# print("foo".center(20))
# print("bar".center(20,"-"))
# print("a\tb\tc".expandtabs())
# print("aaa\tbbb\tc".expandtabs())
# print("a\tb\tc".expandtabs(4))
# print("a\tb\tc".expandtabs(tabsize=4))

# Task 129 
# left-justified "foo", with width 20 and argument"-"
# rigth-justified "foo", with width 10 and argument"-"
# remove http:// from "http://python.org",than remove python
# remove .org from "http://python.org",,than remove python
# remove whitespace in "   foo bar baz"
# remove "http://" with method lstrip in http://realpython.com
# input 42 -> 00042, +0000042, 42
# input "foo" -> 000foo

# print("foo".ljust(20, "-"))
# print("foo".rjust(20, "-"))
# print("http://python.org".removeprefix("http://"))
# print("http://python.org".removeprefix("python"))
# print("http://python.org".removesuffix(".org"))
# print("http://python.org".removesuffix("python"))
# print("   foo bar baz".lstrip())
# print("http://realpython.com".lstrip(":/htp"))
# print("42".zfill(5))
# print("+42".zfill(8))
# print("-42".zfill(8))
# print("42".zfill(2))
# print("foo".zfill(6))

# Task 130
# join list with ", " ["foo", "bar", "baz", "qux"] 
# do same here ["foo", 23, "bar"] #ERR
# print(", ".join(["foo", "bar", "baz", "qux"]))
# print("--".join(["foo", 23, "bar"]))

# Task 131
# join numbers 1 -> 2 -> 3
# numbers = [1, 2, 3]
# print("-> ".join(str(number) for number in numbers))

# Task 132
# partition "foo.bar" with ".", "foo@@bar@@baz" with @@
# "foo.bar@@" with "@@"
# "foo.bar" with "@@"
# partition and than repartition "foo@@bar@@baz" with "@@"
# split "foo bar baz qux"
# split "foo.bar.baz.qux" with sep "."
# split "foo...bar" with sep "."
# split foo\t\t\tbar"
# split "foo.bar.baz.qux" with sep "." and maxsplit 1
# rsplit "foo.bar.baz.qux" with sep "." and maxsplit 1

# print("foo.bar".partition("."))
# print("foo@@bar@@baz".partition("@@"))
# print("foo.bar@@".partition("@@"))
# print("foo.bar".partition("@@"))
# print("foo@@bar@@baz".partition("@@"))
# print("foo@@bar@@baz".rpartition("@@"))
# print("foo bar baz qux".split())
# print("foo.bar.baz.qux".split("."))
# print("foo...bar".split("."))
# print("foo\t\t\tbar".split())
# print("foo.bar.baz.qux".split(".", 1))
# print("foo.bar.baz.qux".rsplit(".", 1))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Introduction to Strings in Python <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Task 133
# concatenate # string1 = "Hello" and # string1 = "Hello" as output --> "Hello World"
# remove spaces in # text = "  Hello World    "
# split text = "Hello World" and "apple, banana,cherry" as substring in list

# string1 = "Hello"
# string2 = "World"
# print(string1 + " " + string2)

# text = "  Hello World    "
# print(text.strip())
# text = "Hello World"
# print(text.split())
# text = "apple,banana,cherry"
# print(text.split(","))

# Task 133
# in text = "Hello World" replace World with Python
# in "Hello World" find World and Python

# print(text.replace("World", "Python"))
# text = "Hello World"
# print(text.find("World"))
# print(text.find("Python"))

# Task 134
# name = "Alice", age = 25 format with %, than with format(), than with f-string
# --> "My name is Alice and i am 25 years old"
# than print "My name is Alice and i am 50 years old"

# name = "Alice"
# age = 25
# print("My name is %s and i am %d years old" % (name, age))
# print("My name is {} and i am {} years old".format(name, age))
# print(f"My name is {name} and i am {age} years old")
# print(f"My name is {name} and i am {age * 2} years old")

# Task 135 !!!! again !!!!
# go in each character with while loop in "Hello World"
# go in each character and index in "Hello World"

# s = "Hello World"
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

# s = "Hello World"
# for i in enumerate(s):
#     print(i)

# Task 136    !!! again !!!
# write a function that reverses "Zviad Kvara" -- > Kvara Zviad

# def reverse(s):
#         words = s.split()
#         words = words[::-1]
#         return " ".join(words)
# print(reverse("Zviad Kvara"))

# Task 137    !!! again !!!
# find the first occurrence of "o" in a string s = "Hello World"
# print first occurence of o is at index 4

# s = "Hello World"
# char = "o"
# index = s.index(char)
# print(f"First occurence of {char} is at index {index}")

# Task 138      !!! again !!!
# find the first occurrence of "z" in a string s = "Hello World"
# if error occurs print "character not found"

# s = "Hello World"
# char = "z"
# try:
#     index = s.index(char)
#     print("First occurrance of",char,"at index", index)
# except ValueError:
#     print("Character not found")

# Task 139 ------------------------------------------------------------>
# find the first occurrence of "o" in a string s = "Hello World"
# using find()

# s = "Hello World"
# char = "o"
# index = s.find(char)
# print("First occurence of",char,"is at", index)

# Task 140
# find the first occurrence of "z" in a string s = "Hello World"
# using find(),if error occurs print "Character not found"

# s = "Hello World"
# char = "z"
# index = s.find(char)
# if index != -1:
#     print("First occurrence of",char,"is at index",index)
# else:
#     print("Charatcer not found")

# Task 141
# find the first occurrence of "o" in a string 
# s = "Hello World" if error occurs print "Character not found" 
# s = "Hello World"
# char ="o"

# for i in range(len(s)):
#     if s[i] == char:
#         print("First occurrence of",char,"is at index",i)
#         break
#     else:
#         print("Character not found")

# Task 142
