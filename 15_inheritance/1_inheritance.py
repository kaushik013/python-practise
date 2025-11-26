

# ⁡⁣⁣⁢inheritance = one class (child class) getting properties, methods of another class(parent class)⁡
# 
# ⁡⁣⁢⁣help to code reuse
# support hierarchy, polymorphism⁡


# ⁡⁣⁣⁢Types of Inheritance in Python⁡
# ⁡⁣⁢⁣Python supports 5 main types of inheritance:⁡


# ⁡⁢⁣⁣Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance⁡

 
class Factory:   # parent class / super claass
    a = 'this is a class attribute'

    def greet(self):
        print('hello good morning!')
    
class FactoryGuj(Factory):  # child class / sub class
    pass

obj1 = Factory()

obj2 = FactoryGuj()
obj2.greet()



# ⁡⁢⁣⁢example⁡


# ⁡⁢⁣⁣1⁡ ⁡⁢⁣⁣single inheritance ⁡
class Univercity:

    loc = 'Ahmedabad,380001'

    def __init__(self,name,collge):
        self.name = name
        self.college = collge

    def uni_show(self):
        print(self.name)
        print(self.college)
        print(f'self.loc \n')

class College(Univercity):
    def __init__(self, name, collge,city):
        super().__init__(name, collge)
        self.city = city 

    def college_show(self):
        print(self.name)
        print(self.college)
        print(self.city)
        print(self.loc)
    

student2 = Univercity('kaushik','gujarat univercity')
student2.uni_show()

student1 = College('janvi','girl college', 'Vadodra')
student1.college_show()


