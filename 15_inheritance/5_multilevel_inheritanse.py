

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
class User:
    def __init__(self, username, phone):
        self.username = username
        self.phone = phone

    def validate_phone(self):
        return len(self.phone) == 10 and self.phone.isdigit()


# Class 2: Customer (inherits User)
class Customer(User):
    def __init__(self, username, phone, customer_id):
        super().__init__(username, phone)
        self.customer_id = customer_id
        self.wallet_balance = 0

    def add_money(self, amount):
        self.wallet_balance += amount
        print(f"₹{amount} added to wallet")

    def show_balance(self):
        print(f"Wallet Balance: ₹{self.wallet_balance}")


# Class 3: PrimeCustomer (inherits Customer)
class PrimeCustomer(Customer):
    def __init__(self, username, phone, customer_id, prime_level):
        super().__init__(username, phone, customer_id)
        self.prime_level = prime_level

    def get_cashback(self, amount):
        if self.prime_level == "Gold":
            return amount * 0.05
        elif self.prime_level == "Platinum":
            return amount * 0.10
        elif self.prime_level == "Diamond":
            return amount * 0.15
        else:
            return 0

    def purchase(self, amount):
        cashback = self.get_cashback(amount)
        final_amount = amount - cashback

        if final_amount <= self.wallet_balance:
            self.wallet_balance -= final_amount
            print(f"Purchase Amount: ₹{amount}")
            print(f"Cashback: ₹{cashback}")
            print(f"Final Amount Paid: ₹{final_amount}")
            print(f"Remaining Wallet Balance: ₹{self.wallet_balance}")
        else:
            print("Insufficient wallet balance")


# Example Usage
pc = PrimeCustomer("kaushik", "9876543210", 101, "Platinum")

print("Phone Valid:", pc.validate_phone())

pc.add_money(1000)
pc.purchase(500)
