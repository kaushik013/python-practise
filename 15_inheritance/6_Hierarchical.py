
#//! hierachical inheritance is a type of inheritance n which multiple child classes inherit from  a single parent class 

#* One Parent → Many Children

#//! Syntax 

# class Parent:
#     # parent class code

# class Child1(Parent):
#     # child1 code

# class Child2(Parent):
#     # child2 code



#//! Example
# class Car:

#     def __init__(self,model):
#         self.model = model

#     def show(self):
#         print(self.model)

# class Fortuner(Car):

#     def __init__(self, model,color):
#         super().__init__(model)
#         self.color = color
    
#     def show(self):
#         print(self.model)
#         print(self.color)
    
# class Audi(Car):

#     def __init__(self, model, price):
#         super().__init__(model)
#         self.price = price

#     def show(self):
#         print(self.model)
#         print(self.price) 


# car1 = Car('Fortuner')
# car1.show()

# car2 = Fortuner(2.98,'white')
# car2.show()

# car3 = Audi(7.0,9000000)
# car3.show()



# Create a Python program that demonstrates Hierarchical Inheritance where:
# One parent class is Employee
# Two child classes are Manager and Developer
# Parent class has a method work()
# Manager class has a method manage()
# Developer class has a method code()


# class Employee:

#     def work(self):
#         print('i am a employee of relience')


# class Manager(Employee):

#     def manage(self):
#         print('manage the all department')
    
# class Developer(Employee):

#     def code(self):
#         print('i am developer')

# obj1 = Manager()
# obj1.work()
# obj1.manage()

# obj2 = Developer()
# obj2.work()
# obj2.code()


# class A:

#     a = 10
#     def __init__(self,value):
#         self.value = value
    
#     @staticmethod
#     def show():
#         return 'I am class A'
    
# class B(A):

#     b = 20
#     def __init__(self, value2):
#         self.value2 = value2
    
#     @staticmethod
#     def show():
#         return 'I am class B'
    

# class C(A):

#     c = 30 
#     def __init__(self, value3):
#         self.value3 = value3
    
#     @staticmethod
#     def show():
#         return 'i am class C'
    

# class D(B,C):

#     d = 40
#     # pass

#     def __init__(self, value4):
#         self.value4 = value4
    
#     @staticmethod
#     def show():
#         return 'I am class D'
    

# obj = D(100)
# print(obj.show())




# ! example
# import random

# class SocialMedia:

#     def __init__(self, user_name, password, followers, following, story):
#         self.uid = random.randint(11111,99999)
#         self.user_name = user_name
#         self.password = password
#         self.followers = followers
#         self.following = following
#         self.story = story

#     def details(self):
#         return self.user_name, self.password, self.followers, self.following, self.story
    

#     def add_followers(self):
#         self.followers += 1
    
#     def remove_following(self):
#         self.following -= 1


# class Snap(SocialMedia):

#     lis = ['username : ','password : ','followers : ','following : ','story : ','stricks : ']
#     def __init__(self, user_name, password, followers, following, story, stricks):
#         super().__init__(user_name, password, followers, following, story)
#         self.stricks = stricks
    
#     def details(self):
#         ttl = super().details()
#         total = ttl + (self.stricks,)
#         return total


# class Facebook(SocialMedia):

#     lis = ['username : ','password : ','followers : ','following : ','story : ','videos : ']

#     def __init__(self, user_name, password, followers, following, story, video):
#         super().__init__(user_name, password, followers, following, story)
#         self.video = video
    
#     def details(self):
#         ttl = super().details()
#         total = ttl + (self.video,)
#         return total
    


# obj = Snap('Kaushik_13',1234,50,10,3,500)

# for i,j in zip(Snap.lis,obj.details()):
#     print(i,j)

# obj1 = Facebook('Ram',12345,300,200,5,10)
# for i,j in zip(Facebook.lis,obj1.details()):
#     print(i,j)