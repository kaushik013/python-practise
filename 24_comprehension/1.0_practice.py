

# 1.  **Program to extract string from the list only if it is palindrome** 
# l= ['hi',100,3.2,'madam','appa','bye' ]

# 2. **Get the following output**
# s = 'programs based open comprehension happy
# out = ['programs','bd','open','cn','hy']



# 3. **Get the following output**
# out=[('A',1),('A',2),('A',3),('B',1)('B',2),('B',3)]


# 4. **Flatten a nested list** 
# n= [[1, 2], [3, 4], [5, 6]]
# output=[1,2,3,4,5,6]


# 5. **Convert Temperatures into Fahrenheit** 
# temp= [0, 20, 37, 100]
# convert each to Fahrenheit using formula
# F = (C * 9/5) + 32

# ## 6. Given below are two list  name  is the list consisting of  name of students and marks are marks of the respective students

# **students = ["Ananya", "Rohit", "Sneha","Aarav","Meera","Karan","Isha","Vivek", "Tanya","Rahul"]**

# **marks = [85, 72, 90, 67, 88,76, 95, 60, 82, 78]**

# ## 1. Extract the names of students whose names start with A

# ## 2. Give a list consisting the name followed by the marks of  particular student

# ## 3. list of  of students getting more than average marks

# ## 4. Create a list of grades (`"A"`, `"B"`, `"C"`) for each student based on their marks:

# - A → Marks ≥ 85
# - B → 70 ≤ Marks < 85
# - C → Marks < 70




#! extract string if it is pallindrom

a = ['hi',100,3.2,'madam','appa','bye']

lis = []

for i in a:
    if(type(i) == str):
        if(i == i[::-1]):
            lis.append(i)
# print(lis)


# restlt = [i for i in a if type(i) == str and i == i[::-1]]
# print(restlt)



#! 2. **Get the following output**
# s = 'programs based open comprehension happy
# out = ['programs','bd','open','cn','hy']

s = 'programs based open comprehension happy'

lis = []
for i in s.split():
    if(len(i) % 2 == 0):
        lis.append(i)
    else:
        lis.append(i[0]+i[-1])
# print(lis)


result = [i if len(i) % 2 == 0 else i[0]+i[-1] for i in s.split()]
# print(result)



#! 3. **Get the following output**
#! 4 = var = [val1,val2 for var1 in collection 1 for var2 in collection 2]
# out=[('A',1),('A',2),('A',3),('B',1)('B',2),('B',3)]

a = ['A','B']
b = [1,2,3]

lis = []

for i in a:
    for j in b:
        lis.append((i,j))
# print(lis)


result = [(i,j) for i in a for j in b]
# print(result)




#! 4. **Flatten a nested list** 
n= [[1, 2], [3, 4], [5, 6]]
# output=[1,2,3,4,5,6]

lis = []

for i in n:
    for j in i:
        lis.append(j)
# print(lis)

        
result = [j for i in n for j in i]
# print(result)



# 5. **Convert Temperatures into Fahrenheit** 
# convert each to Fahrenheit using formula
# F = (C * 9/5) + 32

temp= [0, 20, 37, 100] 

lis = []

for i in temp:
    lis.append(i * 9/5 + 32)
# print(lis)

result1 = [(i * 9/5) + 32 for i in temp]
# print(result1)



# ## 6. Given below are two list  name  is the list consisting of  name of students and marks are marks of the respective students

# **students = ["Ananya", "Rohit", "Sneha","Aarav","Meera","Karan","Isha","Vivek", "Tanya","Rahul"]**

# **marks = [85, 72, 90, 67, 88,76, 95, 60, 82, 78]**

# ## 1. Extract the names of students whose names start with A

# ## 2. Give a list consisting the name followed by the marks of  particular student

# ## 3. list of  of students getting more than average marks

# ## 4. Create a list of grades (`"A"`, `"B"`, `"C"`) for each student based on their marks:

# - A → Marks ≥ 85
# - B → 70 ≤ Marks < 85
# - C → Marks < 70



a = ["Ananya", "Rohit", "Sneha","Aarav","Meera","Karan","Isha","Vivek", "Tanya","Rahul"]
marks = [85, 72, 90, 67, 88,76, 95, 60, 82, 78]

# ## 1. Extract the names of students whose names start with A

lis = []
for i in a:
    if(i[0] == 'A'):
        lis.append(i)
# print(lis)

result = [i for i in a if i[0] == 'A']
# print(restlt)



#! ## 2. Give a list consisting the name followed by the marks of  particular student

lis = []

for i in range(len(a)):
    lis.append([a[i], marks[i]])
# print(lis)


result = [(i,j) for i,j in zip(a,marks)]
# print(result)



#! ## 3. list of  of students getting more than average marks
total = 0
le = len(marks)


for i in marks:
    total += i
# print(total

avg = total/le
 
lis = []
for i,j in zip(a,marks):
    if(j >= avg):
        lis.append(i)
# print(lis)


result = [i for i,j in zip(a, marks) if j > avg]
# print(result)



#! ## 4. Create a list of grades (`"A"`, `"B"`, `"C"`) for each student based on their marks:

# - A → Marks ≥ 85
# - B → 70 ≤ Marks < 85
# - C → Marks < 70

lis = []

for i in marks:
    if(i >=  85):
        lis.append('A')
    elif(i >= 70 and i < 85):
        lis.append('B')
    else:
        lis.append('C')
# print(lis)


result  = ['A' if i  >= 85 else 'B' if i >= 70 else 'C' for i in marks]
# print(result)



