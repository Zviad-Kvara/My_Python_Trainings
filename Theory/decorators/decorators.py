# 1. What happens when you pass a function name without parentheses?

# the function name without parentheses is a reference to the function itself, in thise case
# we are not calling function.

# example 
# def say_hello(name):
#     return f"Hello {name}"

# print(say_hello)

# 2. How does a function work when passed as an argument?
# the recieiving function can call passed function by using its reference
# example

# def greet(name):
#     return f"Hello {name}"

# def x_func(func):
#     return func("Bob")

# print(x_func(greet))

# 3. Can you assign a function to a variable and call it later?
# Yes, you can assign a function to a variable, the variable acts
# as a reference to the function

# def greet(name):
#     return f"Hello {name}"

# say_hey = greet

# print(say_hey("Alice"))

# 4. What are inner functions?
# inner functions are functions which is defined inside another function
# show me an exmaple

# def outer():
#     print("outer function")

#     def inner():
#         print("inner function")

#     inner()
# outer()

# 5. When are inner functions created?
# inner functions created when the outer function is called
# exmaple
# def outer():
#     def inner():
#         return "Inner created!"
#     print("Outer function")
#     return inner

# func = outer() 
# print(func())   

# 6.Can you call an inner function directly from outside its parent?
# no inner functions are locally scoped to the parent function
# and can't be accessed directly
# show me the example

# def outer():
#     def inner():
#         return "Inner function"
#     return "Outer function"

# print(outer())

# 7. Can inner functions be returned or assigned?
# yes we can assign inner functions to use it outside the parent function
# show me the example

# def outer():
#     def inner():
#         return "inner function"
#     return inner

# func = outer()
# print(func())

# 8. Can a function return another function?
# yes function can return another function.returning the functin
# without parentheses gives a reference to function itself, not its execution
# show me the example

# def outer():
#     def inner():
#         return "Inner function is returned"
#     return inner

# returned = outer()
# print(returned())

# 9. What does it mean when the returned function shows a 
# memory address?
# the memory address indicates that the variable is a reference
# to the function.it points to the function stored in memory
# show me an example
# def outer():
#     def inner():
#         return "I am inner function"
#     return inner

# ref = outer()

# print(ref)

# 10. what means first-class objects?
# this means that functions can be passed and used as arguments
# just like any other object
# show me the example

# def say_hello(name):
#     return f"Hello {name}"

# def greet_bob(func):
#     return func("Bob")

# print(greet_bob(say_hello))

# 11. What is a Python decorator?
# a decorator is a function that takes another function as input 
# and returns new function, which modifies the behavior of original funcion
# show me the example

# def decorator(func):
#     def wrapper():
#         print("First whee")
#         func()
#     return wrapper

# def say_whee():
#     print("Whee !")

# say_whee = decorator(say_whee)
# say_whee()

# 12. What is the purpose of the wrapper function?
# the wrapper function adds additional behavior before and after
# the execution of the original function

# Adding Syntactic Sugar
# 13. What does the @ symbol (pie syntax) do in Python?
# it used to apply decorator to the original function.it means
# original funcion repliced with decorated version function
# show me the example
# def decorator(func):
#     def wrapper():
#         print("add vanilas")
#         func()
#     return wrapper

# @decorator
# def ice_cream():
#     print("This is your ice cream")

# ice_cream()

# 14. Why is the @ syntax called syntactic sugar?
# because we don't need to change the original functions body

# 15. Can the @ syntax be used with multiple decorators? 
# yes we can use multiple decorators, they are applied from 
# bottom to top
# show me the example 
# def decorator1(func):
#     def wrapper():
#         print("Add vanilas")
#         func()
#         print("Add cream")
#     return wrapper

# def decorator2(func):
#     def wrapper():
#         print("add sugar")
#         func()
#         print("add more sugar")
#     return wrapper

# @decorator1
# @decorator2
# def ice_cream():
#     print("This is your ice cream")

# ice_cream()

# Decorating Functions With Arguments
# 16. Can decorators be used for functions 
# that accept arguments? 
# yes, but inner wrapper functions in the decorator
# should accept arbitrary arguments using *args and **kwargs
# show me the example
# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper

# def say_hello(name):
#     print(f"Hello {name}")

# say_hello("Ana")

# 17. What are *args and **kwargs in Python?
# *args allows function to accept positional arguments, **kwargs
# allow function to accept keywordarguments
# show me the example

# def func(*args, **kwargs):
#     print("Positional arguments: ", args)
#     print("Keyword arguments: ", kwargs)

# func(1, 2, 3, name="Alex", age=28)

# 18. can decorator change the return value of the decorated function?
# yes decorator can return different value based on the return value
# of the decorated function. we can control whats returned in the wrapper
# show me the example
# def mod(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return f'MODIFIED: {result}'
#     return wrapper

# @mod
# def greet(name):
#     print("Hello someone")
#     return f"Hello {name}"

# print(greet("Adam"))

# 19. What is introspection in Python?
# instrospection is python's ability to know about object's
# attributes at runtime
# give me an example

# print(print.__name__)

# 20. how functools.wraps work?
# functools.wraps decorator preserves the metadata like __name__
# and __doc__ of the original function
# show me the example

# import functools

# def twice(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper

# @twice
# def say_whee():
#     print("Whee!")

# print(say_whee.__name__)

# 21. Why is functools.wraps(func) used in the decorator?
# functools.wraps(func) is used to preserve the original functions
# metadata, such as name and docstring

# import functools
# import time

# def timer(func):
#     """Print the runtime of the decorated function"""
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__}() in {run_time:.4f} secs")
#         return value
#     return wrapper

# @timer
# def waste_time(num_times):
#     for _ in range(num_times):
#         sum([number**2 for number in range(10_000)])
        
        
# waste_time(1)

# 22. Debugging Code
# whas is debug decorator do?
# debug decorator prints the argument passed to the function and the return
# value every time the decorated function is called.
# example 1
# from DECORATORS import debug

# @debug
# def greeting(name, age=None):
#     if age is None:
#         return f"Howdy {name}!"
#     else:
#         return f"Whoa {name}! {age} years old"
    
# # print(greeting("Adam"))
# # print(greeting("Juan", age=30))
# print(greeting(name="Maria", age=28))

# example 2
# DECORATOR and CALCULATE is in another file
#  
# from CALCULATE_E import approximate

# approximate(terms=5)

# 23. Slowing Down Code
# what this code will print and why?
# import functools
# import time

# def slow_down(func):
#     """Sleep 1 second before calling the function"""
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):    
#         time.sleep(5)               
#         return func(*args, **kwargs) 
#     return wrapper

# @slow_down
# def countdown(number):
#     if number < 1:
#         print("Liftoff!")
#     else:
#         print(number)
#         countdown(number - 1)

# countdown(3)

# 24. Registering Plugins
# what will be output and why?
# PLUGINS = dict()
# def register(func):
#     """Register a function as a plug-in"""
#     PLUGINS[func.__name__] = func                    
#     return func                                                                

# @register
# def say_hello(name):
#     return f"Hello {name}"

# @register
# def be_awesome(name):
#     return f"Yo {name} you are cool"

# import random
# def randomly_greet(name):
#     greeter, greeter_func = random.choice(list(PLUGINS.items()))
#     return greeter_func(name)

# print(randomly_greet("Alice"))

# ----------------------------------------- CLASSES SKIPPED  !!!!!!! ---------------------------------------
# 25. what it will print?
# from DECORATORS import debug, do_twice
# import functools
# def debug(func):                # wrapper_debug = wrapper_do_twice
#     @functools.wraps(func)
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]  
#         signature = ", ".join(args_repr + kwargs_repr) 
#         print(f"Calling {func.__name__}()({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__}() returned {repr(value)}")
#         return value
#     return wrapper_debug

# def do_twice(func):              # wrapper_do_twice = greet(name)
#     @functools.wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice

# @debug
# @do_twice
# def greet(name):
#     print(f"Hello {name}")

# greet("Ana")

# 26. what will be output
# from DECORATORS import debug, do_twice
# import functools
# def debug(func):               
#     def wrapper_debug(*args, **kwargs):                                       
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]  
#         signature = ", ".join(args_repr + kwargs_repr) 
#         print(f"Calling {func.__name__}()({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__}() returned {repr(value)}")
#         return value
#     return wrapper_debug

# def do_twice(func):              
#     @functools.wraps(func)                                                    
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice

# @do_twice
# @debug
# def greet(name):
#     print(f"Hello {name}")

# greet("Ana")

# 27. write repeat function that prints Hello World 4 times
# from DECORATORS import repeat
# import functools

# @repeat(num_times=4)
# def greet(name):
#     print(f"Hello {name}")

# greet("World")

# 28.Creating Decorators With Optional Arguments
# what will be output and why?
# import functools

# def repeat(_func=None, *, num_times=2):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper_repeat(*args, **kwargs):
#             for _ in range(num_times):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper_repeat
    
#     if _func is None:
#         return decorator_repeat
#     else:
#         return decorator_repeat(_func)

# @repeat(num_times=4)
# def say_whee():
#     print("Whee!")
                 
# @repeat
# def greet(name):
#     print(f"Hello {name}")

# say_whee()
# greet("Penny")

# 29. what will be output and why?         
# import functools
# def count_calls(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.num_calls += 1
#         print(f"Call {wrapper.num_calls} of {func.__name__}")
#         return func(*args, **kwargs)
#     wrapper.num_calls = 0
#     return wrapper

# @count_calls
# def say_whee():
#     print("Whee!")
# say_whee()
# say_whee()
# print(say_whee.num_calls)

# Function attributes
# https://rushter.com/blog/python-function-features/

# 30. what will be output and why?
# def func():
#     print(func.a)
#     func.a = func.a - 10
#     print(func.a)

# func.a = 10
# func.foo = "bar"
# func()
# func.a = func.a + 2
# func()
# print(func.a)
# print(func.foo)
# print(func.__dict__)

# 31. count the calls of the function with attribute
# def func(a, b):
#     return a + b

# func(1, 2)
# func(2, 5)

# 32. what are function attributes in Python?
# function attrubutes are custom attributes that can be attached to a function
# they can store additional data of a function

# 33. How can you define a custom function attribute? Provide an example.
# we can define a cutom function attribute with dot and assigning value to it

# def say_hello():
#     say_hello.count += 1
#     return "Hello"

# say_hello.count = 0
# say_hello()
# say_hello()
# say_hello()

# print(say_hello.count)

# 34. How can you access a function's custom attributes?
# we can access function custom attributes with dot or __dict__ attrubute
# provide an example
# def say_hello():
#     return "Hello"

# say_hello.data = "Hello"
# say_hello.count = 1

# print(say_hello.data)
# print(say_hello.__dict__)

# 35. Can a function's attributes be modified?
# yes we can modify function attributes just like variables
# provide an example

# def func():
#     print(func.value)

# func.value = 10
# func()
# func.value = 7
# func()

# 36. How can you use function attributes to count the number of times a function is called?
# def func():
#     func.count += 1
#     print(f"function called {func.count} times")

# func.count = 0
# func()
# func()
# print(func.count)

# 37.Why is it generally recommended to avoid using custom function attributes?
# it make code harder to read and understand.

# 38. what will be output and why?
# import functools
# import time
# def slow_down(_func=None, *, rate=1):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             time.sleep(rate)
#             return func(*args, **kwargs)
#         return wrapper
    
#     if _func is None:
#         return decorator
#     else:
#         return decorator(_func)

# @slow_down(rate=2)
# def countdown(number):
#     if number < 1:
#         print("Liftoff!")
#     else:
#         print(number)
#         countdown(number - 1)

# countdown(3)

# 39. what will be output and why?
# import functools
# def count_calls(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.num_calls += 1
#         print(f"Call {wrapper.num_calls} of {func.__name__}")
#         return func(*args, **kwargs)
#     wrapper.num_calls = 0
#     return wrapper

# @count_calls
# def fibonacci(num):
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
# fibonacci(3)

# what will be output and why?
# def recursion(k):
#     if(k>0):
#         result = k + recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
# recursion(3)

# what will be output and why?

# def recursion(k):
#     if k == 0: 
#         return 0
#     result = k + recursion(k - 1) 
#     print(result)  
#     return result
# recursion(3)

# what will be output and why?
# def count(k):
#     if k == 0:
#         return k
#     print(k)
#     count(k - 1)

# print(count(3))

# what will be output and why?
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(3))

# 40. what'll be output and why?
# from DECORATORS import cache, count_calls
# import functools

# @cache 
# @count_calls
# def fibonacci(num):
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
# print(fibonacci(3))

# 41. what will be output and why

# import functools 

# @functools.lru_cache(maxsize=4)
# def fibonacci(num):
#     if num < 2:
#         value = num
#     else:
#         value = fibonacci(num - 1) + fibonacci(num - 2)
#     print(f'Calculated fibonacci ({num}) = {value}')
#     return value

# fibonacci(3)


# ______________________ decorators finished _____________
# decorators tutorial link :  https://realpython.com/primer-on-python-decorators/