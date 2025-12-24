

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


