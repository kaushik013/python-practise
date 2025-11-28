

# class Student:
#     name = 'kaushik'
#     age = 22
#     mail = 'chariyakaushik13@gmail.com'
#     add = 'at,veraval'


#     def info(self):
#         print(f'my name is {self.name} and my age is {self.age}')



# Student.name = 'janvii'

# a = Student()
# a.name = 'kajal'
# a.age = 22
# a.info()

# b = Student()
# b.info()


# class Student:

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def avg_mrk(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print(f'{self.name} your total sum is {sum} and avg is {sum / 3}')


# std = Student('janvi',[87,97,78])
# std.avg_mrk()

# std.name = 'kaushik'
# std.avg_mrk()




def details(a):
    store = []
    while a > 0:
        temp = a % 10
        store.append(temp)
        a //= 10
    for i in range(len(store)-1,-1,-1):
        print(store[i])
       
details(23)



