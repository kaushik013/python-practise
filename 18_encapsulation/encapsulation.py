

#! 🔒 What is Encapsulation?

# Encapsulation means wrapping data (variables) and methods (functions) together inside a class and restricting direct access to the data.

#* we can't access it in outside a class

# Data is protected and accessed only through methods.


#? Why Encapsulation is Needed?
# ✅ Data protection (security)
# ✅ Prevents accidental changes
# ✅ Improves code maintainability
# ✅ Controls how data is accessed


#& 1️⃣ Public Members
#& 2️⃣ Protected Members (_)
#& 3️⃣ Private Members (__)


#^ 1️⃣ Public Members
# Accessible everywhere
# No underscore used

# Example   

class Student:
    def __init__(self, name):
        self.name = name   # public variable

s = Student("Kaushik")
# print(s.name)



#^ 2️⃣ Protected Members (_)
# Accessible inside class & child class
# Should not be accessed directly (by convention)

#! Example
# class Bank:

#     _a = 50000

#     def __init__(self,_name):    #! _name is a protected variable
#         self.name = _name

# obj = Bank('HDFC')

# print(obj._a)
# print(obj.name)



#^ 3️⃣ Private Members (__)
# Accessible only inside the class
# Python uses name mangling


# class Bank:

#     def __init__(self,__acc_num, __balance):
#         self.__acc_num = __acc_num
#         self.__balance = __balance

#     def show(self):
#         print(self.__acc_num)
#         print(self.__balance)

# obj = Bank(12345,9000000)
# obj.show()


#! Example
# class Student:

#     def __init__(self,):
#         self.__mark = 0

#     def get_mark(self):
#         return self.__mark

#     def set_mark(self, mrk):
#         if(mrk >= 0 and mrk <= 100):
#             self.__mark = mrk
#         else:
#             print('invalid mark')
        

# obj = Student()
# print(obj.get_mark())
# obj.set_mark(100)
# print(obj.get_mark())




# class Bank:

#     __branch_manager = 'Dhaval Agrawal'

#     def __init__(self, account_no, balance):
#         self.__account_no = account_no
#         self.__balance = balance
    

# obj = Bank(123456,90000)
# print(obj.__account_no)
# print(obj.__balance) 
# print(obj.__branch_manager)
        

# ! example

# class A:

#     __a = 12

#     def __init__(self,value1,value2):
#         self.__value1 = value1
#         self.__value2 = value2

    # def show(self):
    #     return self.__value1,self.__value2

    # def __show(self):
    #     return self.__value1,self.__value2

# obj = A(12,13)
# print(obj.__show())



# ! example

class Bank:

    __name = 'HDFC Bank'
    __Branch = 'Navrangpura'


    def __init__(self,Accno,balance):
        self.__Accno = Accno
        self.__balance = balance
    
    def getter_balance(self):
        return self._Bank__balance

    def setter_balance(self,new):
        self.__balance += new

    @classmethod
    def name(cls):
        return cls._Bank__name, cls._Bank__Branch
    

obj = Bank(12313,50000)
print(obj.getter_balance())
obj.setter_balance(10000)
print(obj.getter_balance())
print(Bank.name())

        