
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


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print(self.name)
        print(self.age)
    
    def common(self):
        print('Person Version')

class Company:

    def __init__(self, company_name, locaction):
        self.company_name = company_name
        self.locaction = locaction
    
    def show_company(self):
        print(self.company_name)
        print(self.locaction)

    def common(self):
        print('Company Version')

class Employee(Person, Company):

    def __init__(self, name, age, company_name, locaction, salary, role):
        super().__init__(name, age)
        Company.__init__(self,company_name, locaction)
        self.salary = salary
        self.role = role

    def show_employee(self):
        self.show_person()
        self.show_company()
        print(self.salary)
        print(self.role)
        self.common()
    

emo1 = Employee('janvi',21,'Microsoft','Pune',100000,'AI-ML')
emo1.show_employee()

