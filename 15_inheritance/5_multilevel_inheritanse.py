

# this is a basic case where we will have grandparet class, parent class, child class

# Grandparent class ---> Parent class ---> child class



# Q1. Create classes using Multilevel Inheritance:
# Class 1: Person
# Attributes: name, age
# Method: show_person()
# Class 2: Employee (inherits Person)
# Attributes: employee_id, salary
# Method: show_employee()
# Class 3: Manager (inherits Employee)
# Attributes: department
# Method: show_manager()


# class Person:

#     name = 'kaushik'
#     age = 22

#     def show_person(self):
#         print(self.name)
#         print(self.age)

# class Employee(Person):

#     employee_id = 1234
#     salary = 50000

#     def show_employee(self):
#         print(self.employee_id)
#         print(self.salary)

# class Manager(Employee):

#     department = 'IT'

#     def show_manager(self):
#         print(self.department)

# obj = Manager()
# obj.show_person()
# obj.show_employee()
# obj.show_manager()






# Class 1: User
# Attributes:
# username = "kaushik"
# phone = "9876543210"
# Method:
# validate_phone()
# → Return True if phone number has 10 digits, else False.
# Class 2: Customer (inherits User)
# Attributes:
# customer_id = 101
# wallet_balance = 0
# Methods:
# add_money(amount) → add money to wallet
# show_balance()
# Class 3: PrimeCustomer (inherits Customer)
# Attribute:
# prime_level = "Platinum" # (Gold / Platinum / Diamond)
# Methods:
# get_cashback(amount)
# Cashback Rules:
# Gold → 5%
# Platinum → 10%
# Diamond → 15%
# purchase(amount)
# → final_amount = amount − cashback
# → deduct from wallet_balance
# → print final wallet balance



# Class 1: User
# class User:
#     def __init__(self, username, phone):
#         self.username = username
#         self.phone = phone

#     def validate_phone(self):
#         return len(self.phone) == 10 and self.phone.isdigit()


# # Class 2: Customer (inherits User)
# class Customer(User):
#     def __init__(self, username, phone, customer_id):
#         super().__init__(username, phone)
#         self.customer_id = customer_id
#         self.wallet_balance = 0

#     def add_money(self, amount):
#         self.wallet_balance += amount
#         print(f"₹{amount} added to wallet")

#     def show_balance(self):
#         print(f"Wallet Balance: ₹{self.wallet_balance}")


# # Class 3: PrimeCustomer (inherits Customer)
# class PrimeCustomer(Customer):
#     def __init__(self, username, phone, customer_id, prime_level):
#         super().__init__(username, phone, customer_id)
#         self.prime_level = prime_level

#     def get_cashback(self, amount):
#         if self.prime_level == "Gold":
#             return amount * 0.05
#         elif self.prime_level == "Platinum":
#             return amount * 0.10
#         elif self.prime_level == "Diamond":
#             return amount * 0.15
#         else:
#             return 0

#     def purchase(self, amount):
#         cashback = self.get_cashback(amount)
#         final_amount = amount - cashback

#         if final_amount <= self.wallet_balance:
#             self.wallet_balance -= final_amount
#             print(f"Purchase Amount: ₹{amount}")
#             print(f"Cashback: ₹{cashback}")
#             print(f"Final Amount Paid: ₹{final_amount}")
#             print(f"Remaining Wallet Balance: ₹{self.wallet_balance}")
#         else:
#             print("Insufficient wallet balance")


# # Example Usage
# pc = PrimeCustomer("kaushik", "9876543210", 101, "Platinum")

# print("Phone Valid:", pc.validate_phone())

# pc.add_money(1000)
# pc.purchase(500)



# class Car:

#     def __init__(self,brand):
#         self.brand = brand
    
#     def show(self):
#         print(self.brand)

# class Toyota(Car):

#     def __init__(self, brand, model, price):
#         super().__init__(brand)
#         self.model = model
#         self.price = price
    
#     def show(self):
#         super().show()
#         print(self.price)

# class Fortuner(Toyota):

#     def __init__(self, brand, model, price, color, type):
#         super().__init__(brand, model, price)
#         self.color = color
#         self.type = type

#     def show(self):
#         super().show()
#         print(self.color)
#         print(self.type)


# car1 = Fortuner('Toyota','26.1-Landovre',7500000,'back','petrol')
# car1.show()


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


# class Whehical:

#     def __init__(self,brand):

#         self.brand = brand

#     def show(self):
#         return  self.brand

# class Car(Whehical):

#     def __init__(self, brand, name):
#         super().__init__(brand)
#         self.name = name
    
#     def show(self):
#         ttl = super().show()
#         total = ttl + ' ' + self.name
#         return  total
    
# class Electric(Car):

#     def __init__(self, brand, name, Electric_name):
#         super().__init__(brand, name)
#         self.Electric_name = Electric_name
    
#     def show(self):
#         ttl = super().show()
#         total = ttl + ' ' + self.Electric_name
#         return total
    
# obj = Electric('Toyota','Fortuner','Enova')
# # print(obj.show())

# li = ['The brand is : ','Fuel car is : ','Electric car is : ']
# spl =  obj.show()

# for i,j in zip(li,spl.split()):
#     print(i,j)

