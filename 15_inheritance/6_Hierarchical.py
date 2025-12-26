
#//! hierachical inheritance is a type of inheritance n which multiple child classes inherit from  a single parent class 

#* One Parent → Many Children

#//! Syntax 

# class Parent:
#     # parent class code

# class Child1(Parent):
#     # child1 code

# class Child2(Parent):
#     # child2 code



#//! Example
# class Car:

#     def __init__(self,model):
#         self.model = model

#     def show(self):
#         print(self.model)

# class Fortuner(Car):

#     def __init__(self, model,color):
#         super().__init__(model)
#         self.color = color
    
#     def show(self):
#         print(self.model)
#         print(self.color)
    
# class Audi(Car):

#     def __init__(self, model, price):
#         super().__init__(model)
#         self.price = price

#     def show(self):
#         print(self.model)
#         print(self.price) 


# car1 = Car('Fortuner')
# car1.show()

# car2 = Fortuner(2.98,'white')
# car2.show()

# car3 = Audi(7.0,9000000)
# car3.show()



# Create a Python program that demonstrates Hierarchical Inheritance where:
# One parent class is Employee
# Two child classes are Manager and Developer
# Parent class has a method work()
# Manager class has a method manage()
# Developer class has a method code()


# class Employee:

#     def work(self):
#         print('i am a employee of relience')


# class Manager(Employee):

#     def manage(self):
#         print('manage the all department')
    
# class Developer(Employee):

#     def code(self):
#         print('i am developer')

# obj1 = Manager()
# obj1.work()
# obj1.manage()

# obj2 = Developer()
# obj2.work()
# obj2.code()


# class A:

#     a = 10
#     def __init__(self,value):
#         self.value = value
    
#     @staticmethod
#     def show():
#         return 'I am class A'
    
# class B(A):

#     b = 20
#     def __init__(self, value2):
#         self.value2 = value2
    
#     @staticmethod
#     def show():
#         return 'I am class B'
    

# class C(A):

#     c = 30 
#     def __init__(self, value3):
#         self.value3 = value3
    
#     @staticmethod
#     def show():
#         return 'i am class C'
    

# class D(B,C):

#     d = 40
#     # pass

#     def __init__(self, value4):
#         self.value4 = value4
    
#     @staticmethod
#     def show():
#         return 'I am class D'
    

# obj = D(100)
# print(obj.show())