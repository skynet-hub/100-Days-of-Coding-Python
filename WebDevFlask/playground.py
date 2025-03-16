# from flask import Flask
import time

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return '<p>Hello, World!</p>'

# if __name__ == '__main__':
#     app.run()

# def add(n1, n2):
#     return n1 + n2

# def multiply(n1, n2):
#     return n1 * n2

#Functions in python are treated as first class objects, they can be passed into other functions like strings,integers and floats
#Another interesting about functions is they can be returned inside other functions

# def calculate(fun, n1, n2):
#     return fun(n1, n2)

# print(calculate(multiply, 3, 6))

# #Look at this nice example for returning nested dunctions, NB all this is foundational to understanding python decorators

# def outer():
#     print('I am outer')

#     #Here's a nested function
#     def inner():
#         print('I am inner')
#     return inner

# inner_function = outer()  #Saving inner function in this varible, Notice this will also trigger the outer function.
# inner_function() #Now we trigger the inner funcrion    

# #A decorator function is just a function that wraps another and gives it additional functionality or modifies the functionality

# def decorator_function(fun):
#     def wrapper():
#         fun()
#     return wrapper  #Without paranthesis because we are not looking to call it at this point    

# def delay_decorator(fun):
#     def wrapper():
#         time.sleep(2)
#         #You can do somethings before the functions
#         fun() #More interesting you can modify the function maybe call it twice
#         #You can do something after the function
#     return wrapper

# @delay_decorator
# def Hello():
#     print('Hello')      

# Hello()    

class User:
    def __init__(self, user):
        self.name = user
        self.is_logged_in = False

def decorated_authentication(fun):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            fun(args[0]) 
    return wrapper               

@decorated_authentication
def is_logged(user):
    print(f'User {user.name} is logged on')        

new_user = User('Dave')
new_user.is_logged_in = True
is_logged(new_user)  