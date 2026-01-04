

#! ⁡⁣⁣⁢inheritance = one class (child class) getting properties, methods of another class(parent class)⁡
# 
# ⁡⁣⁢⁣help to code reuse
# support hierarchy, polymorphism⁡


# ⁡⁢⁣⁢__init__⁡
# ⁡⁢⁣⁣it is a special method
# when  object create then __init__ automatically run

#! __init__ is a constructor used to initialize object properties when the object is created.


#! ⁡⁢⁣⁢Super()⁡

# ⁡⁢⁣⁣super() means go to the parent class and used its methods

# ⁡⁢⁣⁣Jyaare tame child class banaavo ane parent class ni method / constructor ne use karvu hoy, 
# tyaare super() help kare che.


# ⁡⁣⁣⁢Types of Inheritance in Python⁡
# ⁡⁣⁢⁣Python supports 5 main types of inheritance:⁡


# ⁡⁢⁣⁣Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance⁡

 
# class Factory:   # parent class / super claass
#     a = 'this is a class attribute'

#     def greet(self):
#         print('hello good morning!')
    
# class FactoryGuj(Factory):  # child class / sub class
#     pass

# obj1 = Factory()

# obj2 = FactoryGuj()
# obj2.greet()



# ⁡⁢⁣⁢example⁡


# ⁡⁢⁣⁣1⁡ ⁡⁢⁣⁣single inheritance ⁡
# class Univercity:

#     loc = 'Ahmedabad,380001'

#     def __init__(self,name,collge):
#         self.name = name
#         self.college = collge

#     def uni_show(self):
#         print(self.name)
#         print(self.college)
#         print(f'self.loc \n')

# class College(Univercity):
#     def __init__(self, name, collge,city):
#         super().__init__(name, collge)
#         self.city = city 

#     def college_show(self):
#         print(self.name)
#         print(self.college)
#         print(self.city)
#         print(self.loc)
    

# student2 = Univercity('kaushik','gujarat univercity')
# student2.uni_show()

# student1 = College('janvi','girl college', 'Vadodra')
# student1.college_show()


  
# class Bank:
#     branch = 'Ahmedabad'

#     def __init__(self,balance):
#         self.balance = balance
    

# class Emp(Bank):

#     def __init__(self, balance,name):
#         # super() it is used to access the parent method and constructor 
#         super().__init__(balance)
#         self.name = name

    
#     def show(self):
#         print(self.branch)
#         print(f'Bank balance is : {self.balance}')
#         print(f'Bank holder name is : {self.name}')

# emp = Emp(100000,'Kaushik')
# emp.show()



# # ^ example

# class Bank:

#     name = 'ICICI'
#     brance = 'Ahmedabad'
#     manager = 'Ashok shah'

#     def __init__(self,name,accno,balance):
#         self.name = name
#         self.accno = accno
#         self.balance = balance
    
#     def show(self):
#         print(self.name)
#         print(self.accno)
#         print(self.brance)

#     @classmethod
#     def dicply_cls(cls):
#         print(cls.name)
#         print(cls.brance)
#         print(cls.manager)

    

# class Another_Bank(Bank):
#     loc = 'at.junagadh'


#     def __init__(self, name, accno, balance,branch_code):
#         self.name = name
#         self.accno = accno
#         self.balance = balance
#         self.branch_code = branch_code

#     def show(self):
#         print(self.name)
#         print(self.accno)
#         print(self.brance)
#         print(self.branch_code)
    
#     @classmethod
#     def dicply_cls(cls):
#         print(cls.name)
#         print(cls.brance)
#         print(cls.manager)
#         print(cls.loc)

    
    

# c1 = Another_Bank('kaushik',90905,10000,'Veraval')
# c1.show()
# c1.dicply_cls()
        
        

