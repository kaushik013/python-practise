
# Hybrid Inheritance is a type of inheritance that is formed by combining two or more types of inheritance (like single, multiple, multilevel, hierarchical).

# # syntax

# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass


# # Example

# class Person:
#     def show_person(self):
#         print("I am a person")

# class Employee(Person):
#     def show_employee(self):
#         print("I am an employee")

# class Student(Person):
#     def show_student(self):
#         print("I am a student")

# class Intern(Employee, Student):
#     def show_intern(self):
#         print("I am an intern")

# Object
# obj = Intern()
# obj.show_person()
# obj.show_employee()
# obj.show_student()
# obj.show_intern()


#! example 

# class A:
#     a = 10

# class B(A):
#     b = 20

# class C(A):
#     pass

# class D(B,C):
#     d = 40

# obj = D()
# print(D.mro())
# print(obj.a)


# import random
# class University:

#     Uni_name = 'Gujarat technical University'
#     address = 'Ahmedabad'

#     def __init__(self,name,contact):
#         self.name = name
#         self.contact = contact
#         self.UID = random.randint(11111,99999)
    
#     def info(self):
#         return self.name,self.contact,self.UID


# class Commerce(University):

#     HOD = 'Ritesh Agrawal'

#     def __init__(self, name, contact,sub):
#         super().__init__(name, contact)
#         self.sub = sub
    
#     def info(self):
#         ttl = super().info()
#         total = ttl + (self.sub,)
#         return total

# class Science(University):

#     HOD = 'Dharmesh Rawal'

#     def __init__(self, name, contact,sub):
#         super().__init__(name, contact)
#         self.sub = sub
    
#     def info(self):
#         ttl = super().info()
#         total = ttl + (self.sub,)
#         return total

# class Stream(Commerce,Science):

#     def __init__(self, name, contact, sub,stream):
#         super().__init__(name, contact, sub)
#         self.stream = stream
    
#     def info(self):
#         ttl =  super().info()
#         total = ttl + (self.stream,)
#         return total

# obj = Stream('Kaushik',9016883191,'Account','B.com')
# print(obj.info())



    