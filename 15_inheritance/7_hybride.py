
# Hybrid Inheritance is a type of inheritance that is formed by combining two or more types of inheritance (like single, multiple, multilevel, hierarchical).

# syntax

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass


# Example

class Person:
    def show_person(self):
        print("I am a person")

class Employee(Person):
    def show_employee(self):
        print("I am an employee")

class Student(Person):
    def show_student(self):
        print("I am a student")

class Intern(Employee, Student):
    def show_intern(self):
        print("I am an intern")

# Object
# obj = Intern()
# obj.show_person()
# obj.show_employee()
# obj.show_student()
# obj.show_intern()




