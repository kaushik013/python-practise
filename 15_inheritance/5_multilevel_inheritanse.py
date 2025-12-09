

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



# class User:

#     username = "kaushik"
#     phone = "9876543210"

#     def validate_phone(self):
#         if(len(self.phone) >= 10):
#             return True
#         else:
#             return False
        
# class Customer(User):

#     customer_id = 101
#     wallet_balance = 0

#     def add_money(self,amount):
#         self.amount = amount
#         self.wallet_balance += amount

#     def show_balance(self):
#         print(self.wallet_balance)


# class PrimeCustomer(Customer):
    






# Phone Valid: True
# Money Added: 500
# Purchase Amount: 2000
# Cashback (10%): 200.0
# Final Deducted Amount: 1800.0
# Remaining Wallet Balance: -1300.0



