
# ⁡⁢⁣⁡⁣⁣⁢OOPS = Object Oriented Programming System⁡


# ⁡⁢⁣⁣oops is a way to write a program using object⁡

# ⁡⁢⁣⁣an object is a...⁡

# ⁡⁣⁢⁣You create classes (templates)
# And from those classes, you create objects (real things)
# Objects have properties (data) and functionalities (methods)


# ✔ ⁡⁣⁢⁣Object is NOT a property⁡
# ✔ ⁡⁣⁢⁣Object is NOT a functionality
# ⁡⁢⁣⁢⭐ Object contains both properties and functionalities.


# ⁡⁣⁣⁢Main Goals of OOPS⁡
# ⁡⁢⁣⁣Manage big programs easily
# Reuse code
# Reduce complexity
# Provide security to data⁡


# ⁡⁢⁣⁣all advanced concept⁡

# ⁡⁣⁢⁣✔ FULL                        OOPS SUMMARY
# Concept	                    Meaning
# Class             	        Blueprint
# Object	                    Instance
# Constructor	                Auto-run method
# Encapsulation     	        Data hiding
# Abstraction	                Hide internal details
# Inheritance	                Parent → Child
# Polymorphism	                One name, many forms
# Overriding	                Child changes method
# Overloading	                Same method, diff params
# Operator Overloading      	Change operator meaning
# Class Method	                Works with class
# Static Method	                Normal method
# Composition	                Class inside class
# Property	                    Getter/Setter⁡


# ⁡⁣⁢⁣how to create class⁡ 

class Car:
    pass

c1 = Car()   # object
c2 = Car()   # another object


# second 
class Student:
    college = 'Gujarat University'

# object 
std = Student()
print(std.college)


# class 
class  Bike:
    feature = 'Most power ful Engine'

bike1 = Bike()
print(bike1.feature)



class Factory:
    a = 12
    
    def hello(self):
        print('hello coder!')
    
    print('hello what can i help you!')

print(Factory().a)
Factory().hello()




# ⁡⁢⁣⁣class attribute, instance attribute, instance method, @classmethod, @staticmethod⁡

class Bag:
    company = 'american tourist!'   # ⁡⁢⁣⁢class attribute⁡

    def __init__(self,color,price):
        self.color = color        # ⁡⁢⁣⁢instance attribute⁡
        self.price = price
    

    def show(self):              # ⁡⁢⁣⁢instance method⁡
        print(self.color, self.price)


    @classmethod
    def hello(cls):
        print('hello how are you!')


    @staticmethod
    def hii():
        print('hii it is okey!')



#  ⁡⁢⁣⁣object⁡ 
bag1 = Bag('black',9999)
bag1.show()
bag1.hello()
bag1.hii()


         




# ⁡⁢⁣⁣all class have __init__ function ⁡
# ⁡⁣⁢⁣Used to initialize data when object is created.⁡


# ⁡⁢⁣⁣what is self⁡

class ABC:
    def __init__(self):
        print(self)
        # ⁡⁣⁢⁣<__main__.ABC object at ⁡⁣⁣⁢0x101974ad0⁡>⁡

s1 = ABC()



#⁡⁢⁣⁣ Example⁡
class Apple:
    def __init__(self,brand,price,color):
        self.Brand = brand
        self.Price = price
        self.Color = color

    def info(self):
        print(f'the brand is {self.Brand} price is {self.Price} and color is {self.Color}')
    
iphone = Apple('Iphone 17Air',120000,'Blue')
Macbook = Apple('Macbook M1Air',75000,'Midnight')
Watch = Apple('Watch',12000,'Pink')
ipad = Apple('Ipad',55000,'black')


#⁡⁢⁣⁡⁢⁣⁣ how to modify value⁡
iphone = Apple('Iphone 16',75000,'purple')

# ⁡⁢⁣⁣access value⁡
iphone.info()
Macbook.info()
Watch.info()
ipad.info()



