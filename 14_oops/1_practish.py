
class Student:
    def __init__(self,name,age,city,college):
        self.Name = name
        self.Age = age
        self.City = city
        self.College = college

    def colleges(self):
        print('student of ',self.College)
    

    def details(self):
        self.colleges()
        print(f'my name is {self.Name} my age is {self.Age} i am from {self.City} and my college is {self.College} \n')



Student1 = Student('kaushik','22','ahmedabad','IIM')
Student2 = Student('Raj','21','veraval','Parul UNI')
Student3 = Student('Janvi','20','vadodra','Girls college')


Student1.details()
Student2.details()
Student3.details()



# ********************************************************************************************************



# class 

# class Car:


    # Constructor (runs automatically when object is created)

#     def __init__(self,name,color,price):
#         self.Name = name
#         self.Color = color
#         self.Price = price 
   
#     def start(self):
#         print(self.Name, 'is starting.....')

#     def details(self):
#         self.start()
#         print(f'the brand name is {self.Name} colore is {self.Color} and price is {self.Price} \n')



# # creating a object 

# car1 = Car('BMW','Black',10000000)
# car2 = Car('Farari','White',1200000)


# car1.details()
# car2.details()



