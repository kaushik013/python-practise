
# Create two parent classes:
# Class Teacher → method teach() prints "Teaching..."
# Class Coach → method teach() prints "Coaching..."
# Create a child class Tutor that inherits from both.
# 👉 When you call teach() using Tutor object, which method runs?
# (Write the code and output.)


# class Teacher:

#     def teach(self):
#         print('Teaching...')


# class Coach:

#     def teach(self):
#         print('Coaching...')

# class Tutor(Teacher,Coach):
#     pass


# obj = Tutor()
# obj.teach()
    




# # Create two parent classes:
# # Class Parent1 → method show() prints "Parent1 show"
# # Class Parent2 → method show() prints "Parent2 show"
# # Create child class Child(Parent1, Parent2).
# # 👉 Do NOT override the method in Child.
# # 👉 Create an object of Child and call show().
# # Which show() executes and why?
# # (Write code + output.)


# class Parent1:

#     def show(self):
#         print('Parent 1 show')


# class Parent2:

#     def show(self):
#         print('Parent2 show')

# class Child(Parent1,Parent2):
#     pass

# obj = Child()
# obj.show()


# Parent Classes
# Class Engine
# Constructor → print("Engine Started")
# Method engine_info() → print("1200 CC Engine")
# Class Body
# Constructor → print("Body Created")
# Method body_info() → print("Sedan Body")
# Child Class
# Class Car(Engine, Body)
# Do not override constructors.
# Create a method details() that calls both:
# engine_info()
# body_info()
# Requirements
# 👉 Create a Car object.
# 👉 Which constructor runs and why?
# 👉 Print the output.



# class Engine:
#     def __init__(self):
#         print('Engine Started...')

#     def engine_info(self):
#         print('1200 CC Engine')

    
# class Body:

#     def __init__(self):
#         print("Body Created")

#     def body_info(self):
#         print("Sedan Body")


# class Car(Engine,Body):

#     def detail(self):
#         self.engine_info()
#         self.body_info()
    

# obj = Car()
# obj.detail()


# # Class Account
# # Constructor → prints "Account Created"
# # Method → acc_info() prints "Account Info"
# # Class Customer
# # Constructor → prints "Customer Registered"
# # Method → cust_info() prints "Customer Info"
# # Class Bank(Account, Customer)
# # Constructor →
# # Use super() inside constructor
# # Print "Bank Object Ready"
# # Method → show_all()
# # Call:
# # acc_info()
# # cust_info()


# class Account:

#     def __init__(self):
#         print('Account Created')

#     def acc_info(self):
#         print('Account Info')
    

# class Customer:

#     def __init__(self):
#         print('Customer Registered')
    
#     def cust_info(self):
#         print('Customer Info')


# class Bank(Account,Customer):

#     def __init__(self):
#         super().__init__()
#         print('Bank Object Ready')
    
#     def show_all(self):
#         self.acc_info()
#         self.cust_info()

    
# obj = Bank()
# obj.show_all()



# 1️⃣ Class X
# Constructor → prints "X init"
# Method show() → prints "X show"
# 2️⃣ Class Y(X)
# Constructor → calls super().__init__()
# Print "Y init"
# Method show() → prints "Y show"
# 3️⃣ Class Z(X)
# Constructor → calls super().__init__()
# Print "Z init"
# Method show() → prints "Z show"
# 4️⃣ Class P(Y, Z)
# Constructor → calls super().__init__()
# Print "P init"
# Method show() → calls super().show() then prints "P show"
# Tasks
# Create object:
# obj = P()
# Call method:
# obj.show()
# Write exact output and explain why using MRO.
# This is the most complex pure multiple inheritance scenario you can practice in Python.
# Do you want me to give the full solution with output, Kaushiksir?


# class X:

#     def __init__(self):
#         print('X init')

#     def show(self):
#         print('X show')

# class Y(X):

#     def __init__(self):
#         super().__init__()
#         print('Y init')

#     def  show(self):
#         print('Y show')

    
# class Z(X):

#     def __init__(self):
#         super().__init__()
#         print('Z init')

#     def show(self):
#         print('Z show')


# class P(Y,Z):

#     def __init__(self):
#         super().__init__()
#         print('P init')
    
#     def show(self):
#         super().show()
#         print('P show')
    

# obj = P()
# obj.show()



# Class 1: PersonalInfo
# Attributes: name, age, phone
# Method: show_personal()
# Class 2: BankAccount
# Attributes: account_no, balance
# Method: show_bank()
# Class 3: LoanDetails
# Attributes: loan_id, loan_amount, interest_rate
# Method: calculate_interest()
# (Return yearly interest)
# Class 4: Customer (inherits from PersonalInfo, BankAccount, LoanDetails)
# Add method: show_full_details()
# It should print:

# class PersonalInfo:

#     name = 'kaushik'
#     age = 22
#     phone = 9016883191

#     def show(self):
#         print(self.name)
#         print(self.age)
#         print(self.phone)

# class BankAccount:

#     Account_no = 314102010264218
#     balance = 50000


#     def show_bank(self):
#         print(self.Account_no)
#         print(self.balance)


# class LoanDetails:

#     loan_id = 1313
#     loan_amount = 1000000
#     interest_rate = 10

#     def calculate_interest(self):
#         return self.loan_amount * self.interest_rate / 100
    
# class Customer(PersonalInfo,BankAccount,LoanDetails):

#     def show_full_details(self):
#         self.show()
#         print()

#         self.show_bank()
#         print()

#         yearly_intrest = self.calculate_interest()

#         print('loan amount : ',self.loan_amount)
#         print('intrest rate : ', self.interest_rate,'%')
#         print('yearly_intrest rate : ',yearly_intrest)

#         total = self.balance + self.loan_amount + yearly_intrest
#         print('total payable amount : ',total)

# obj = Customer()
# obj.show_full_details()



# Class: Employee
# Attributes: emp_id, emp_name
# Method: show_employee()
# Constructor must print "Employee init"
# Class: Salary
# Attributes: basic_salary, allowance
# Method: calculate_salary() → return basic_salary + allowance
# Constructor must print "Salary init"
# Class: Performance
# Attributes: rating (1–5)
# Method: bonus_amount()
# If rating ≥ 4 → bonus = 20% of basic_salary
# Else → bonus = 10% of basic_salary
# # Constructor must print "Performance init"


# class Employee:

#     emp_id = 60754181
#     emp_name = 'kaushik'

#     def show_employee(self):
#         print('enp id is : ',self.emp_id)
#         print('emp name is : ',self.emp_name)

#     def __init__(self):
#         print('Employee init')
    

# class Sallery:

#     basic_salary = 50000
#     allowance = 5000


#     def calculate_salary(self):
#         return self.basic_salary + self.allowance


#     def __init__(self):
#         print('Salary init')

# class Performance(Employee,Sallery):

#     ratting = 5

#     def bonus_amount(self):
#         if(self.ratting > 4):
#             return self.basic_salary + 20 / 100
#         else:
#             return self.basic_salary + 10 /100
        

#     def __init__(self):
#         super().__init__()
#         print('Performance init')

