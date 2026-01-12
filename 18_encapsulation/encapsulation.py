

#! 🔒 What is Encapsulation?

# Encapsulation means wrapping data (variables) and methods (functions) together inside a class and restricting direct access to the data.

#* we can't access it in outside a class

# Data is protected and accessed only through methods.


#? Why Encapsulation is Needed?
# ✅ Data protection (security)
# ✅ Prevents accidental changes
# ✅ Improves code maintainability
# ✅ Controls how data is accessed


#& 1️⃣ Public Members
#& 2️⃣ Protected Members (_)
#& 3️⃣ Private Members (__)


#^ 1️⃣ Public Members
# Accessible everywhere
# No underscore used

# Example   

class Student:
    def __init__(self, name):
        self.name = name   # public variable

s = Student("Kaushik")
# print(s.name)



#^ 2️⃣ Protected Members (_)
# Accessible inside class & child class
# Should not be accessed directly (by convention)

#! Example
# class Bank:

#     _a = 50000

#     def __init__(self,_name):    #! _name is a protected variable
#         self.name = _name

# obj = Bank('HDFC')

# print(obj._a)
# print(obj.name)



#^ 3️⃣ Private Members (__)
# Accessible only inside the class
# Python uses name mangling


# class Bank:

#     def __init__(self,__acc_num, __balance):
#         self.__acc_num = __acc_num
#         self.__balance = __balance

#     def show(self):
#         print(self.__acc_num)
#         print(self.__balance)

# obj = Bank(12345,9000000)
# obj.show()


#! Example
# class Student:

#     def __init__(self,):
#         self.__mark = 0

#     def get_mark(self):
#         return self.__mark

#     def set_mark(self, mrk):
#         if(mrk >= 0 and mrk <= 100):
#             self.__mark = mrk
#         else:
#             print('invalid mark')
        

# obj = Student()
# print(obj.get_mark())
# obj.set_mark(100)
# print(obj.get_mark())




# class Bank:

#     __branch_manager = 'Dhaval Agrawal'

#     def __init__(self, account_no, balance):
#         self.__account_no = account_no
#         self.__balance = balance
    

# obj = Bank(123456,90000)
# print(obj.__account_no)
# print(obj.__balance) 
# print(obj.__branch_manager)
        

# ! example

# class A:

#     __a = 12

#     def __init__(self,value1,value2):
#         self.__value1 = value1
#         self.__value2 = value2

    # def show(self):
    #     return self.__value1,self.__value2

    # def __show(self):
    #     return self.__value1,self.__value2

# obj = A(12,13)
# print(obj.__show())



# ! example

# class Bank:

#     __name = 'HDFC Bank'
#     __Branch = 'Navrangpura'


#     def __init__(self,Accno,balance):
#         self.__Accno = Accno
#         self.__balance = balance
    
#     def getter_balance(self):
#         return self._Bank__balance

#     def setter_balance(self,new):
#         self.__balance += new
    
#     @classmethod
#     def getter_branch(cls):
#         return cls._Bank__Branch

#     @classmethod
#     def setter_branch(cls,new):
#         cls._Bank__Branch = new

#     @classmethod
#     def name(cls):
#         return cls._Bank__name, cls._Bank__Branch
    

# obj = Bank(12313,50000)
# print(Bank.getter_branch())
# Bank.setter_branch('SP stadium')
# print(Bank.getter_branch())


# print(obj.getter_balance())
# obj.setter_balance(10000)
# print(obj.getter_balance())
# print(Bank.name())

        
# ! method  over loading 

# class Demo:

#     @staticmethod
#     def demo():
#         print('hii')
    
#     @staticmethod
#     def demo(a):
#         print(a)
#         print('hello')

# Demo.demo(12)


# ! method overriding

# class Parent:

#     @staticmethod
#     def demo():

#         print('hii')
    

# class Child(Parent):

#     @staticmethod
#     def demo(a):
#         print('hello')
#         print(a)
    
# obj = Child()
# obj.demo(12)


# ! monkey paching


# class Parent:

#     @staticmethod
#     def demo():
#         print('i am from  parent class')
    
#     backup = demo
    

# class Child(Parent):
#     @staticmethod
#     def demo(a):
#         print('i am from child class')
#         print(a)
    
# obj = Child()
# obj.demo(12)
# obj.backup()


# ! Example of monkey paching

# class Demo:
#     @staticmethod
#     def sam():
#         print('good evening!')
#     first = sam
    
#     @staticmethod
#     def sam(a,b):
#         print(a,b)
#     second = sam

#     @staticmethod
#     def sam(a,b,c):
#         print(a,b,c)
#     third = sam

# obj = Demo()
# obj.first()
# obj.second(12,13)
# obj.third(12,13,14)


#!  create calss whehical with method drive create sub classes car,bike overriding the drive method

# class Vehical:

#     def drive(self):
#         print('whehical is started...')
    
# class Car(Vehical):

#     def drive(self):
#         print('Car is rinning....')
    
# class Bike(Vehical):
    
#     def drive(self):
#         print('Bike is running')

# obj = Bike()
# obj.drive()


#! demonstrangth inheritance from class person to derived class teacher and perform the following instruction 
#^ base class should have  name and age 
#^ derieved class should add subject 
#^ display all the details using display method 


# class Person:

#     def __init__(self, name , age):
#         self.name = name 
#         self.age = age 

#     def display(self):
#         return self.name, self.age

# class Teacher(Person):

#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject
    
#     def display(self):
#         ttl = super().display()
#         total = ttl + (self.subject,)
#         return total

# lis = ['name is : ','age is : ', 'subject is : ']

# per1 = Teacher('Yashraj',24,'Pythin')

# for i,j in zip(lis,per1.display()):
#     print(i,j)


# ! create class employee with a method calculate calary create two sub classes manager and programer and in each of the sub class override ther calclulate salary method in order to return the salary based on the specific role 

# class Employee: 

#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#         self.base_salary = 10000
        
#     def calculate(self):
#         return self.base_salary

# class Manager(Employee):

#     def __init__(self, name, age,year_exp):
#         super().__init__(name, age)
#         self.year_exp = year_exp

#     def calculate(self):
#         ttl = super().calculate()
#         total = ttl + 10000 * self.year_exp 
#         return total

# class Programmer(Employee):

#     def __init__(self, name, age, year_exp):
#         super().__init__(name, age)
#         self.year_exp = year_exp

#     def calculate(self):
#         ttl = super().calculate()
#         total = ttl + 20000 * self.year_exp
#         return total 

# obj = Manager('kaushik',22,3)
# print('total manager salary : ',obj.calculate())


# obj1 = Programmer('dharmesh',23,2)
# print('total programmer salary  : ',obj1.calculate())

#! create a class shape with method get area and get perimater and create three sub classes circle, rantangle, square overriding get area and get perimater and each of the sub class 


# class Shape:
#     def get_area(self):
#         pass

#     def get_perimeter(self):
#         pass


# class Circle(Shape):

#     def __init__(self,radius):
#         self.radius = radius
    
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
    
#     def get_perimeter(self):
#         return 2 * 3.14 * self.radius

# class Ractangle(Shape):

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def get_area(self):
#         return self.length * self.width


#     def get_perimeter(self):
#         return 2 * (self.length + self.width)
    

# class Square(Shape):

#     def __init__(self,side):
#         self.side  = side
    
#     def get_area(self):
#         return self.side * self.side
    
#     def get_perimeter(self):
#         return 4 * self.side

# obj = Circle(13)
# print(obj.get_area())
# print(obj.get_perimeter())

       
