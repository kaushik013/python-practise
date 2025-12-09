
# ⁡⁢⁣⁣single inheritance⁡

# Q1.
# ⁡⁢⁣⁣Create a class Animal with method eat().⁡
# ⁡⁣⁢⁣Create another class Dog that inherits from Animal and adds method bark().
# Create object of Dog and call both methods.


# class Animal:
#     def eat(self):
#         print('i am eat paddigree 🦴 ')


# class Dog(Animal):
#     def bark(self):
#         print('bhavvv bhavvv!')

# obj = Dog()
# obj.eat()
# obj.bark()



# Q1.
# ⁡⁢⁣⁣Create a class Animal with method eat().⁡
# ⁡⁣⁢⁣Create another class Dog that inherits from Animal and adds method bark().
# Create object of Dog and call both methods.


# class Animal:
#     def eat(self):
#         print('i am eat paddigree 🦴 ')


# class Dog(Animal):
#     def bark(self):
#         print('bhavvv bhavvv!')

# obj = Dog()
# obj.eat()
# obj.bark()


# #⁡⁢⁣⁣ Create a class Person with attribute name.⁡
# # ⁡⁣⁢⁣Create class Student(Person) that adds attribute rollno.
# # Print student name and rollno using Student object.⁡


# class Person:
    
#     def __init__(self,name):
#         self.name = name

# class Student(Person):

#     def __init__(self, name,rollno):
#         super().__init__(name)
#         self.rollno = rollno

#     def show(self):
#         print(self.name)
#         print(self.rollno)

# obj = Student('janvi',11)
# obj.show()



# ⁡⁢⁣⁣Create a class Shape with method area().⁡
# ⁡⁣⁢⁣Create class Square(Shape) and override area() to print the area of a square.
# Take side as input in constructor
# Print area inside overridden method⁡

# class Shape:
#     def __init__(self,side):
#         self.side = side

#     def area(self):
#         print('area not defined!')


# class Square(Shape):
#     def __init__(self, side):
#         super().__init__(side)
    

#     def area(self):
#         area_val = self.side * self.side
#         print(area_val)

# sqr = Square(5)
# sqr.area()




# ⁡⁢⁣⁣Create a class Vehicle with method start() that prints:⁡
# ⁡⁣⁢⁣Create a class Car(Vehicle) with method speed() that prints:⁡
# ⁡⁣⁢⁣Create an object of Car and call:
# ✔ start() (from parent)
# ✔ speed() (from child)⁡

# class Vehicle:

#     def start(self):
#         print('car is startin...')
    
# class Car(Vehicle):

#     def speed(self):
#         print('car is running at 120km/s')


# cr = Car()
# cr.start()
# cr.speed()


# ⁡⁢⁣⁣Create a class Employee with attributes:⁡
# ⁡⁣⁢⁣name
# salary
# Create class Manager(Employee) with attribute:
# department
# Create a method show() in Manager to print:
# Name: ______
# Salary: ______
# Department: ______
# Create object of Manager and print all details.⁡


# class Employee:
    
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    
# class Manager(Employee):

#     def __init__(self, name, salary,department):
#         super().__init__(name, salary)
#         self.department = department

#     def show(self):
#         print(f'Name :......  {self.name}')
#         print(f'Salary :......  {self.salary}')
#         print(f'Department :...... {self.department}')

# obj = Manager('kaushik',100000,'IT')
# obj.show()


# ⁡⁢⁣⁣Create a class BankAccount with:⁡
# ⁡⁣⁢⁣account_no
# balance
# Create class SavingsAccount(BankAccount) with method:
# add_interest(rate)
# → It should increase the balance by the given interest rate.
# (Example: rate = 10 means +10%)
# Example:
# If balance = 1000 and rate = 10
# Final balance = 1100
# Create object and show updated balance.⁡


# class BankAccount:

#     def __init__(self,account_no,balance):
#         self.accunt_no = account_no
#         self.balance = balance
    
# class SavingsAccount(BankAccount):

#     def add_interest(self,rate):

#         intrest_rate =   (self.balance * rate/100)
#         final_balance = self.balance + intrest_rate
#         print(f'you have {rate}% rate in {self.balance} and final balance is {final_balance}')




# user = SavingsAccount(12121313,10000)
# user.add_interest(20)

        

#⁡⁢⁣⁣ Create a class Product with:⁡
# ⁡⁣⁢⁣name
# price
# Create a class DiscountProduct(Product) with:
# Extra attribute → discount (in %)
# Override the constructor and use super()
# Create a method final_price() that prints the price after discount.

# ⁡⁢⁣⁢own logic⁡

# class Product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

# class DiscountProduct(Product):

#     def __init__(self, name, price):
#         super().__init__(name, price)


#     def final_price(self):
#         if(self.price >= 5000):
#             discount = self.price - (self.price * 30//100)
#             print(f'congrats! you have discount {self.price * 30//100} 💵')
#             print(f'your payment is {discount}')
#         elif(self.price >= 3000):
#             discount = self.price - (self.price * 15//100)
#             print(f'congrats! you have discount {self.price * 15//100} 💵')
#             print(f'your payment is {discount}')
#         elif(self.price >= 1000):
#             discount = self.price - (self.price * 5//100)
#             print(f'congrats! you have discount {self.price * 5//100} 💵')
#             print(f'your payment is {discount}')
#         else:
#             print('no any discount 😕')
#             print(f'your payment is {self.price}💵')

# prd = DiscountProduct('FaceWash',5000)
# prd.final_price()




# ⁡⁢⁣⁣Q11. Commission-Based Employee Salary Calculator⁡
# ⁡⁣⁢⁣Create a class Employee with:
# name
# base_salary
# Create class SalesEmployee(Employee) with extra attribute:
# sales_amount
# Add method final_salary() that gives commission:
# Commission Rules:
# If sales ≥ 1,00,000 → 20% commission
# If sales ≥ 50,000 → 10% commission
# If sales ≥ 20,000 → 5% commission
# Else → No commission⁡


# class Employee:

#     def __init__(self,name,base_salary):
#         self.name = name
#         self.base_salary = base_salary


# class SalesEmployee(Employee):

#     def __init__(self, name, base_salary,sales_amount):
#         super().__init__(name, base_salary)
#         self.sales_amount = sales_amount

    
#     def final_salary(self):
#         if(self.sales_amount >= 100000):
#             incentive =  (self.sales_amount * 20//100)
#             final_sal = self.base_salary + incentive
#             print(f'congrats! you have incentive {incentive}')
#             print(f'your total salary is {final_sal} 💵')
#         elif(self.sales_amount >= 50000):
#             incentive =  (self.sales_amount * 10//100)
#             final_sal = self.base_salary + incentive
#             print(f'congrats! you have incentive {incentive}')
#             print(f'your total salary is {final_sal} 💵')
#         elif(self.sales_amount >= 20000):
#             incentive =  (self.sales_amount * 5//100)
#             final_sal = self.base_salary +incentive
#             print(f'congrats! you have incentive {incentive}')
#             print(f'your total salary is {final_sal} 💵')
#         else:
#             print('you have not able to incentive 😕')
#             print(f'your total salary is {self.base_salary} 💵')


# emp1 = SalesEmployee('kaushik',100000,500000)
# emp1.final_salary()






# **Q1. Create a class Person with attributes name and age.
# Create another class Student that inherits from Person and adds a new attribute roll_no.
# Write code to create an object of Student and print all details.**


# class Person:

#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

# class Student(Person):

#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no

#     def show(self):
#         print(f'name is : {self.name}')
#         print(f'age is : {self.age}')
#         print(f'rollno is : {self.roll_no}')

    
# std = Student('kaushik',22,13)
# std.show()

    

# Create a BankAccount base class and a SavingsAccount child class.
# The base class must handle:
# account number, holder name, balance
# deposit()
# withdraw()
# show_balance()
# The child class (SavingsAccount) must add:
# interest_rate
# apply_interest() → adds interest to balance
# A rule: withdrawal cannot exceed balance – 1000 (minimum balance rule)
# Write the classes and show the output for:
# Creating a SavingsAccount
# Depositing money
# Trying to withdraw more than allowed
# Applying interest


import random

account_num  = random.randint(1111111111,9999999999)
name = input('enter your name : ')
age = int(input('enter the age : '))
address = input('enter your address : ')
bank_pin = int(input('enter the 4 digit pin : '))



def show_bank_detail():
    print(f'your account no : {account_num}')
    print(f'your name is : {name}')
    print(f'your age is {age}')
    print(f'your address is :{address}')

a = input('show your bank datail type yes/no : ')

if(a == 'yes'):
    b = int(input('enter the bank-pin : '))
    if(b == bank_pin):
        show_bank_detail()
    else:
        print('incorrect pin!')
else:
    print('thank you!')


class BankAccount:

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposite(self,deposite):
        self.balance += deposite
        print(f'{deposite} amount is cradited !')

    def withdrow(self,withdrow):
        if(withdrow <= self.balance):
            total = self.balance - withdrow
            if( total >= 1000):
                self.balance= self.balance - withdrow
                print('you are success fully withdrow!')
            else:
                print('not withdrow you main tain 1000rs minimyn')
        else:
            print('insaffent balance!')


  


class SavingAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)
        self.auto_apply_intrest()

    def auto_apply_intrest(self):
        if self.balance >= 100000:
            interest = self.balance * 0.10
            self.balance += interest
            print(f'Interest added: {interest}')
        elif self.balance >= 50000:
            interest = self.balance * 0.05
            self.balance += interest
            print(f'Interest added: {interest}')
        else:
            print('not eligible for interest rate!')

    def show_balace(self):
        a = int(input('enter your pin for check balance : : '))
        if(a == bank_pin):
            print(f'your balance is : {self.balance}')
        else: 
            print('wrong pin')



amount = int(input('enter amount to be started added  : '))
emp = SavingAccount(account_num,name,amount)

deposit = int(input('enter the deposite amount : '))
emp.deposite(deposit)

withdrow = int(input('enter the withdrow amount : '))
emp.withdrow(withdrow)

emp.show_balace()


