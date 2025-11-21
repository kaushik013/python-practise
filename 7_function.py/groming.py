

def sum(a,b):
    return a + b

def sqr(d):
    return d * d

d = sum(10,10)
print(sqr(d))





d = 20

def myFunction():
    global d
    c = 2000
    def inner():
        nonlocal c
        c = c + c 
        print(c)
    inner()
myFunction()




def demo2(*args,**kwrgs):
    print(args)
    print(type(args))  # <class 'tuple'>

    print(kwrgs)
    print(type(kwrgs))
demo2(12,23,34,45,65,a=22,b=23)  # <class 'dict'>