

# //& Polymorphism means “one name, many forms.”

# Same method name, but different behavior depending on the object.


#//! Example
# A person can be:
# A teacher in school
# A father at home
# A customer in a shop
# Same person, different roles → this is polymorphism 👍


#//* there are two types 

#//! 1.  Method Overriding
# Method overriding is when a child class uses the same method name as the parent class but gives it a new behavior.

#//! 2. Method Overloading
# Python does not support true overloading, but we can achieve it using default arguments.


# Syntax 

class Parent:
    def method_name(self):
        # parent code
        pass

class Child(Parent):
    def method_name(self):
        # child code (overrides parent method)
        pass


#//^ Example
# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# d = Dog()
# d.sound()


#//! duck typing
# Duck Typing is a concept where Python focuses on what an object can do, not what class it belongs to.


#//! example
class Laptop:
    def work(self):
        print("Laptop is working")

class Human:
    def work(self):
        print("Human is working")

def do_work(obj):
    obj.work()

# do_work(Laptop())
# do_work(Human())


#//! Example
# class Factory:
#     def show(self):
#         print('hello factory')


# class Brand:

#     def show(self):
#         print('hello model')
    
# def show_all(obj):
#     obj.show()

# show_all(Factory())
# show_all(Brand())


