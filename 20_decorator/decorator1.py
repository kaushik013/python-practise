
import time
import datetime


#! decorator

#! 1 inbuilt decorator 

#! 2 user define inbuilt decorator 



#* 1 inbuilt decorator 

#^ @classmethod
#^ @staticmethod



#^ user define inbuilt decorator

#! stntax 

# def decorator_name(func):
#     def wrapper(*argd,**kwargs):
#         PRE-TASK
#         result = func(*args,**kwargs)
#         POST-TASK
#         return result
#     return wrapper


#! Example

def greet(func):
    def wrap(*args,**kwargs):
        print('hello user!')
        result = func(*args,**kwargs)
        print('Thankyou!')
        return result
    return wrap

# @greet
# def demo():
#     print('kaushik')
# demo()


# @greet
# def num(a,b):
#     print(a + b)
# num(12,12)



# def welcome(func):
#     def wraper(*args,**kwars):
#         print('this is the made by developer!')
#         result = func(*args,**kwars)
#         print('thank you !')
#         return result
#     return wraper

# @welcome
# def fact(n):
#     factor = 1
#     for i in range(1,n+1):
#         factor *= i
#     print(factor)
    
# fact(5)


#* Example
#! create a decorator which will calculate total execution time of any function



# def timer(func):
#     def wraper(*args,**kwargs):
#         st = time.time()
#         result = func(*args,**kwargs)
#         et = time.time()
#         print(f'this is the total execution time {et-st:6f}')
#         return result
#     return wraper


def timer(func):
    def wraper(*args,**kwargs):
        st = time.time()
        result = func(*args,**kwargs)
        et = time.time()
        now = datetime.datetime.now()
        print(f"{now:%d-%m-%Y %I:%M:%S %p}")
        return result
    return wraper

@timer
def addition(a,b):
    print(a+b)

addition(13,14)


