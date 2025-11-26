

# Q1.⁡⁢⁣⁣ Create a class Student with attributes name and age.
# ⁡⁣⁢⁣Create 2 objects and print their details.⁡

# class Student:
#     def __init__(self,name,age):
#         self.Name = name
#         self.Age = age
    
#     def details(self):
#         print(f'my name is {self.Name} and my age is {self.Age} \n')
        
# std1 = Student('kaushik',22)
# std2 = Student('Janvi',21)

# std1.details()
# std2.details()



# ✅ ⁡⁢⁣⁣**Q2. Create a class Car with one method start() that prints “Car Started”.⁡

# ⁡⁣⁢⁣Create an object and call the method.**

# 👉 Write the code yourself.
# 👉 After you send your answer, I’ll check and correct it if needed.
# Ready… Go! 🚗💨⁡

# class Car:

#     def start(self):
#         print('Car Started!')

# car1 = Car()
# car1.start()





# ⁡⁢⁣⁣✅ **Q3. Create a class Laptop with variables brand and price.⁡
# ⁡⁣⁢⁣Assign values using a constructor and print them.**⁡

# class Laptop:
  
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price


#     def details(self):
#         print(self.brand,self.price)
    
# laptop1 = Laptop(brand='Macbook',price=80000)
# laptop2 = Laptop(brand='Vivobook',price=50000)

# laptop1.details()
# laptop2.details()



# ⁡⁣⁢⁡⁢⁣⁣✅ **Q4. Create a class Dog with a method bark() that prints “WoofWoof!”.⁡
# ⁡⁣⁢⁣Create an object and call the method.**⁡

# class Dog:
#     def bark(self):
#         print('Woof Woof!')

# dog = Dog()
# dog.bark()





#⁡⁣⁢⁣ ⁡⁢⁣⁣✅ **Q5. Create a class Circle that stores the radius.⁡
# ⁡⁣⁢⁣Add a method area() that prints the area of the circle.**
# Formula:
# Area=3.14×r⁡ 


# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         print(3.14 * self.radius * self.radius)

# c1 = Circle(5)
# c1.area()



# ⁡⁢⁣⁣✅ **Q6. Create a class Employee with attributes id, name, and salary.⁡

# ⁡⁣⁢⁣Add a method show() to print the employee details.
# Create 2 employee objects and display their information.**⁡

# class Employee:
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
    
#     def show(self):
#         print(f'id : {self.id} Name : {self.name} Sallery : {self.salary}')


# emp1 = Employee(1112,'kajal',50000)
# emp2 = Employee(1113,'Raj',80000)
# emp3 = Employee(1114,'kaushik',1000000)

# emp1.show()
# emp2.show()
# emp3.show()


#⁡⁣⁢⁣ ⁡⁢⁣⁣✅ Q7. Create a class Calculator with the following methods:⁡
# add(a, b)
# sub(a, b)
# mul(a, b)
# div(a, b)
# Create an object and call all the methods.⁡⁡

# class Calculator:


#     def add(self,a,b):
#         print('Addition : ',a + b)
    
#     def sub(self,a,b):
#         print('Substraction : ',a-b)
    
#     def mul(self,a,b):
#         print('Multipliction : ',a*b)
    
#     def div(self,a,b):
#         print('Division : ',a/b)


# cal = Calculator()
# cal.add(11,12)
# cal.sub(11,12)
# cal.mul(11,12)
# cal.div(11,12)



# ⁡⁣⁢⁣✅ ⁡⁢⁣⁣Q8. Create a class BankAccount with:⁡
# ⁡⁣⁢⁣Attributes:
# balance

# Methods:
# deposit(amount) → add money
# withdraw(amount) → subtract money
# show_balance() → print balance⁡

# class BankAccount:
#     balance = 0

#     def __init__(self,balance):
#         self.balance = balance
    
#     def deposit(self,amount):
#         self.balance += amount

#     def withdraw(self,amount):
#         self.balance -= amount 

#     def show_balance(self):
#         print(self.balance)


# acc = BankAccount(0)
# acc.deposit(500)
# acc.withdraw(200)
# acc.show_balance()        

        


# ⁡⁢⁣⁣🔟 ATM (hard)**⁡
# ⁡⁣⁢⁣✔ Private pin → self.__pin
# ✔ Method verify(pin):
# if pin matches → return True
# ✔ withdraw() uses verify
# ✔ If wrong → print error
# ✔ If right → balance -= amount⁡



class ATM:
    def __init__(self,pin,balance):
        self.pin = pin
        self.balance = balance

    def verify(self,user_pin):
        return user_pin == self.pin

    def withdraw(self,amount,user_pin):
        if(self.verify(user_pin)):
            if(amount <= self.balance):
                self.balance -= amount
                print(f'{amount} is successfully withdraw!')
                print(f'{self.balance} your balance!')
            else:
                print('you have no money! ')
        else:
            print('incorrect pin ❌')
        
    def show_balance(self,user_pin):
        if(self.verify(user_pin)):
            print(f'{self.balance} your balance!')
        else:
            print('wrong pin ❌')



user = ATM(1313,100000)
user.withdraw(10000,1313)
user.show_balance(1313)




# ⁡⁢⁣⁣static method in oops ⁡
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def greet():
        print('hello!')

    def mark_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print(f'{self.name} your sum is {sum} and avg is {sum/3:.2f}%')

std1 = Student('kaushik',[88,79,98])
std1.mark_avg()
std1.greet()


