

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
#        return self.name,self.accno,self.balance

#     @classmethod
#     def dicply_cls(cls):
#         return cls.name,cls.brance,cls.manager


# class Another_Bank(Bank):
#     loc = 'at.junagadh'

#     def __init__(self, name, accno, balance, branch_code):
#         super().__init__(name, accno, balance)
#         self.branch_code = branch_code

#     def show(self):
#         total = super().show()
#         new = total + (self.branch_code,)
#         return new

#     @classmethod
#     def dicply_cls(cls):
#         clas = super().dicply_cls()
#         total = clas + (cls.loc,)
#         return total

# c1 = Another_Bank('kaushik',90905,10000,'Veraval')
# print('object method : ',c1.show())
# print('class method : ',c1.dicply_cls())
        
        
# # !  Example

# class Parent:

#     def __init__(self, a, b):
#         self.a  = a
#         self.b = b
    
#     def show(self):
#         return self.a, self.b

# class Child(Parent):

#     def __init__(self, a, b, c):
#         super().__init__(a, b)
#         self.c = c

#     def show(self):
#         ttl = super().show()
#         total = ttl + (self.c,)
#         return total

# c1 = Child(12,13,14)
# print(c1.show())



#! if we need some values
# class Parent:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# class Child(Parent):
#     def __init__(self, a, c):
#         super().__init__(a, c)  
#         self.c = c

# c1 = Child(12, 14)
# print(c1.a, c1.c)

# ! create a class school and perform a single level inheritance into another class college by implement constructor chaining as well as method chaining


# class School:

#     def __init__(self, name, mobile, sid):
#         self.name = name
#         self.mobile = mobile
#         self.sid = sid
    
#     def show(self):
#         return self.name, self.mobile, self.sid 

# class College(School):

#     def __init__(self, name, mobile, sid, per, stream):
#         super().__init__(name, mobile, sid)
#         self.per = per
#         self.stream = stream

#     def show(self):
#         ttl = super().show()
#         total = ttl + (self.per, self.stream)
#         College.totalll(total)

#     @staticmethod
#     def totalll(total):
#         print('name : ',total[0])
#         print('mobile no  : ',total[1])
#         print('sid : ',total[2])
#         print('per  : ',total[3])
#         print('stream  : ',total[4])



# std = College('kaushik',9016883191,1213,'90%','commerce')
# # print(std.show())
# std.show()

# # for i in std.show():
# #     print(i)


# class Bank:

#     def __init__(self, balance):
#         self.balance = balance

    
#     def add_balance(self):
#         self.balance += int(input('enter the amount to add : '))
    
#     def withdrow(self):
#         widrw = int(input('enter the withdrow amount : '))
#         if(widrw <= self.balance):
#             total = self.balance - widrw
#             if(total >= 5000):
#                 if(widrw >= 500):
#                     print(f'Success fully withdrowl ! {widrw} ✅')
#                     print('press yes to check balance : ')
#                     inp = input('yes or no  : ')
#                     if(inp == 'yes' or inp == 'Yes'):
#                         print('your balance is : ',self.balance - widrw)
#                         check = input('enter add to deposit : add / no : ')
#                         if(check == 'add'):
#                             ad = int(input('enter the num : '))
#                             self.balance += ad 
#                             print(f'amount cradited! {ad} ✅')
#                         else:
#                             print('thank you!')
#                     else:
#                         print('thank you !')
#                 else:
#                     print('amount must be > 500Rs 🆙')
#             else:
#                 print('please mentain 5000 amount 😕')
#         else:
#             print('insuffacient amount!')
    
    

#     def details(self):
#         return self.balance

# obj = Bank(6000)
# obj.withdrow()
# # print(obj.details())
