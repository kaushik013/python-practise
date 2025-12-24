

#! Decorator

# Decorator ek aisa function hota hai jo dusre function ki functionality ko change ya extend karta hai,

# ! Example
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper



class Animal:

    @property
    def show(self):
        print('hello decorator')
    
# obj = Animal()
# obj.show




# def decorator(func):
#     def wrapper():
#         print('i am first call')
#         func()
#         print('i am last run')
#     return wrapper

# @decorator
# def hello():
#     print('hello i am decorarot')

# hello()


# def names(func):
#     def wrapper(name):
#         print('welcome')
#         func(name)
#         print('thank you')
#     return wrapper

# @names
# def greet(name):
#     print(name)

# greet('kaushik')
