
# ⁡⁢⁣⁣multiple inheritance⁡

# ⁡⁣⁢⁣In multiple inheritance, one child class inherits from two or more parent classes.⁡

# class Father:
    
#     def __init__(self,f_name,f_age):
#         self.f_name = f_name
#         self.f_age = f_age
#         super().__init__()


# class Mother:
#     def __init__(self):
#         self.mother_occupation = 'House Wife'
#         super().__init__()

# class Child(Father,Mother):
#     def __init__(self, f_name, f_age,c_name, c_degree):
#         super().__init__(f_name, f_age)
#         self.c_name = c_name
#         self.c_degree = c_degree


#     def details(self):
#         print(self.f_name)
#         print(self.f_age)
#         print(self.mother_occupation)
#         print(self.c_name)
#         print(self.c_degree)


# std = Child('Pankaj',44,'kajal','MCA')
# std.details()



# Q1.
# ⁡⁢⁣⁣Create classes A and B each having a method show().
# Create class C(A, B) and call the show() method.⁡


# class A:
#     def show(self):
#         print('hello i am A')

# class B:
#     def show(self):
#         print('hello i am B')

# class C(A,B):
#     pass

# obj = C()
# obj.show()



# ⁡⁢⁣⁣Create class Father with attributes:⁡
# ⁡⁣⁢⁣f_name
# f_age
# Create class Mother with attributes:
# m_name
# m_hobby
# Create class Child(Father, Mother) that has its own attributes:
# c_name
# c_age
# 👉 Task:
# Create an object of Child and print all Father, Mother, and Child details.


# class Father:
#     def __init__(self,f_name, f_age):
#         self.f_name = f_name
#         self.f_age = f_age



# class Mother:
#     def __init__(self,m_name,m_hobby):
#         self.m_name = m_name
#         self.m_hobby = m_hobby


# class Child(Father,Mother):

#     def __init__(self, f_name, f_age,m_name,m_hobby, c_name, c_age):
#         Father.__init__(self, f_name, f_age)
#         Mother.__init__(self, m_name,m_hobby)
#         self.c_name = c_name
#         self.c_age = c_age
    
#     def details(self):
#         print(f'Father name : {self.f_name}')
#         print(f'Father age is  : {self.f_age}')
#         print(f'Mother name : {self.m_name}')
#         print(f'Mother Hobby is : {self.m_hobby}')
#         print(f'Child name : {self.c_name}')
#         print(f'Child age is : {self.c_age}')


# obj = Child('varajangbhai',44,'shantiBen','Carring','kaushik',22)
# obj.details()


# Create two classes:
# Class X
# Method: m1() → prints "I am X"
# Class Y
# Method: m1() → prints "I am Y"
# Class Z(X, Y)
# Do NOT create any method in class Z.
# 👉 Task
# Create an object of class Z.
# Call m1() using that object.
# Observe: Which class method is executed?
# Print MRO of class Z.


# class X:

#     def m1(self):
#         print('i Am X')
    
# class Y:
#     def m1(self):
#         print('i Am Y') 

# class Z(X,Y):
#     pass

# boj = Z()
# boj.m1()
# print(Z.__mro__)




# Class 1: Person
# __init__ → name, age
# Method → show_person() → print personal info
# Method → common() → print "Person version"
# Class 2: Company
# __init__ → company_name, location
# Method → show_company() → print company info
# Method → common() → print "Company version"
# Class 3: Employee(Person, Company)
# __init__ → name, age, company_name, location, salary, role
# Use super()
# Method → show_employee() → print employee info
# Print all variables from Person, Company, Employee
# Call common() → find out which one runs (MRO)


# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_person(self):
#         print(self.name)
#         print(self.age)
    
#     def common(self):
#         print('Person Version')

# class Company:

#     def __init__(self, company_name, locaction):
#         self.company_name = company_name
#         self.locaction = locaction
    
#     def show_company(self):
#         print(self.company_name)
#         print(self.locaction)

#     def common(self):
#         print('Company Version')

# class Employee(Person, Company):

#     def __init__(self, name, age, company_name, locaction, salary, role):
#         super().__init__(name, age)
#         Company.__init__(self,company_name, locaction)
#         self.salary = salary
#         self.role = role

#     def show_employee(self):
#         self.show_person()
#         self.show_company()
#         print(self.salary)
#         print(self.role)
#         self.common()
    

# emo1 = Employee('janvi',21,'Microsoft','Pune',100000,'AI-ML')
# emo1.show_employee()



# class A:

#     @staticmethod
#     def demo():
#         return 'i am class A'
    
# class B:

#     @staticmethod
#     def demo():
#         return 'i am class B'

# class C(A,B):
#     # pass

#     @staticmethod
#     def demo():
#         pass
#         return 'I am class C'

# obj = C()
# print(obj.demo())

# ! example 

# class Company:

#     def __init__(self, name, address):
#         self.name = name 
#         self.address = address

#     def show(self):
#         return self.name, self.address
    
# class Google(Company):

#     def __init__(self, name, address, branch, ceo):
#         super().__init__(name, address)
#         self.branch = branch
#         self.ceo = ceo
#         # return ttl + (self.branch, self.ceo)
    
#     def show(self):
#         ttl = super().show()
#         return ttl + (self.branch, self.ceo)
    
# class Employee(Google):

#     def __init__(self, name, address, branch, ceo, ename, salary):
#         super().__init__(name, address, branch, ceo)
#         self.ename = ename
#         self.salary = salary
    
#     def show(self):
#         ttl = super().show()
#         return ttl + (self.ename, self.salary)
    

# obj = Employee('Google','Ahmedabad','Nikol','Aman dhattrwal','kaushik',90000)
# li = ['Company name is  : ','Address is : ','Branch is : ','CEO is : ','Ename is : ','Salary is : ']


# for i,j in zip(li,obj.show()):
#     print(i,j)

#! MRO - method resoluction order
# print(Employee.mro())



# ! Example

# class Grandfather:

#     def __init__(self,grand_father):
#         self.grand_father = grand_father
    
#     def show(self):
#         return self.grand_father

# class Father(Grandfather):

#     def __init__(self, grand_father, father):
#         super().__init__(grand_father)        
#         self.father = father
    
#     def show(self):
#         total = super().show()
#         ttl = self.father + ' ' + total
#         return ttl
    
# class Son(Father):

#     def __init__(self, grand_father, father, name):
#         super().__init__(grand_father, father)
#         self.name = name 
    
#     def show(self):
#         ttl = super().show()
#         total = self.name
#         return total + ' ' + ttl
    
# obj = Son('Omprakash','Sanjay','kabir')
# print(obj.show())


# ! create a class whehical and perform numlti level inheritance in to the other two classes electric car and car 


class Whehical:

    def __init__(self,brand):

        self.brand = brand

    def show(self):
        return  self.brand

class Car(Whehical):

    def __init__(self, brand, name):
        super().__init__(brand)
        self.name = name
    
    def show(self):
        ttl = super().show()
        total = ttl + ' ' + self.name
        return  total
    
class Electric(Car):

    def __init__(self, brand, name, Electric_name):
        super().__init__(brand, name)
        self.Electric_name = Electric_name
    
    def show(self):
        ttl = super().show()
        total = ttl + ' ' + self.Electric_name
        return total
    
obj = Electric('Toyota','Fortuner','Enova')
# print(obj.show())

li = ['The brand is : ','Fuel car is : ','Electric car is : ']
spl =  obj.show()

for i,j in zip(li,spl.split()):
    print(i,j)

