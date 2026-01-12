
# ! Example 

from abc import ABC,abstractmethod

# class Father(ABC):

#     property1 = '100 Acers'
#     property2 = '@ Petrol pump'
#     property3 = '4 Fortuner'


#     @abstractmethod
#     def task():
#         print('this is parent mathod')
    
# class Child(Father):

#     @staticmethod
#     def task():
#         print('this is child method')
        
    
# obj = Child()
# obj.task()
# print(obj.property1,obj.property2,obj.property3)


#! create an abstract class Shape with abstract method-area().
# create subslasses Circlr, Rectangle and  implement area()

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius * self.radius)
    

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    

obj1 = Circle(13)
print(obj1.area())

obj2 = Rectangle(12,13)
print(obj2.area())





















