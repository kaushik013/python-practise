

# ⁡⁣⁣⁢what is list ?⁡

# --- > ⁡⁢⁣⁣list is a collection of item(element) that can be of different data type, such as number, 
# string and even other list⁡


# ⁡⁣⁢⁣l͟i͟s͟t a͟r͟e o͟r͟d͟e͟r, c͟h͟a͟n͟g͟a͟b͟l͟e͟(͟m͟u͟t͟a͟b͟l͟e͟), a͟n͟d a͟l͟l͟o͟w d͟u͟p͟l͟i͟c͟a͟t͟e v͟a͟l͟u͟e⁡

# ⁡⁢⁣⁢Syntax⁡ :

my_lists = ['kaushik', 1, True, 22.44]

print(type(my_lists))
# <class 'list'>


#⁡⁣⁣⁢ lists power ⁡:-

# ⁡⁢⁣⁣1. mutable⁡ ---> ⁡⁣⁢⁣it means it can be change after 

# ⁡⁢⁣⁣2. duplicate⁡ --->⁡⁣⁢⁣ it means it can be accept duplicate value⁡

# ⁡⁢⁣⁣3. ordered⁡ --->  ⁡⁣⁢⁣This means you can access elements using their position (index)⁡

# ⁡⁢⁣⁣4. hetrogenous⁡ ---> ⁡⁣⁢⁣this means it accept multiple data type in list⁡


# ⁡⁣⁣⁢how to create list⁡

my_marks = [99,88,78,98,90,78,87]
print(my_marks)
# [99, 88, 78, 98, 90, 78, 87]


# ⁡⁣⁣⁢how to access element ⁡

access = my_marks[0]
print(access)
# 99

# ⁡⁣⁣⁢how to change value ⁡

my_marks[1] = 100
print(my_marks[1])
# 100


# ⁡⁣⁣⁢how to access element by using loop⁡


# ⁡⁢⁣⁣first way⁡
for i in range(len(my_marks)):
    print(my_marks[i])

# ⁡⁢⁣⁣second way⁡
for i in my_marks:
    print(i)




# ⁡⁣⁣⁢lists method ⁡⁣⁣⁢()⁡

# print(dir(list))

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
'__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
'pop', 'remove', 'reverse', 'sort']


num = [1,3,4,5]

# ⁡⁢⁣⁣append()⁡ ---> ⁡⁣⁢⁣add element in last position⁡
num.append(6)
print(num)
# [1, 2, 3, 4, 5, 6]



# ⁡⁢⁣⁣insert()⁡ ---> ⁡⁣⁢⁣insert element in perticular index⁡

num.insert(1,2)
print(num)
# [1, 2, 3, 4, 5, 6]


# ⁡⁢⁣⁣extend()⁡ ---> ⁡⁣⁢⁣insert multiple element it tha time⁡

# ⁡⁢⁣⁣syntax :⁡ 
# ⁡⁢⁣⁣extend([])⁡

a = [11,22,33,44,55]
a.extend([66,77,88,99])
print(a)
# [11, 22, 33, 44, 55, 66, 77, 88, 99]


# ⁡⁢⁣⁣remove()⁡ ---> ⁡⁣⁢⁣remove element(jo pass karege vo remove ho jayega)⁡

a.remove(22)
print(a)
# [11, 33, 44, 55, 66, 77, 88, 99]


# ⁡⁢⁣⁣pop()⁡ ---> ⁡⁣⁢⁣remove element and we can store the variable⁡
i = ['a','b','c','d','e']
store = i.pop(1)

print(i)
print(store)


# ⁡⁢⁣⁣index()⁡ ---> ⁡⁣⁢⁣find the index of element⁡
k = i.index('a')
print(k)
# 0


# ⁡⁢⁣⁣count()⁡ ---> ⁡⁣⁢⁣return count of exting element⁡
x = [11,11,12,13,14,15,16,17]
y = x.count(11)
print(y)
# 2


# ⁡⁢⁣⁣sort()⁡ ---> ⁡⁣⁢⁣sort the list of assending order⁡
c = [12,42,453,32,1,34,2,44,2,3]
c.sort()
print(c)
# [1, 2, 2, 3, 12, 32, 34, 42, 44, 453]


# ⁡⁢⁣⁣reverse()⁡ ---> ⁡⁣⁢⁣reverse list (start from last)⁡
name = ['kaushik','kanji','ram']
name.reverse()
print(name)
# ['ram', 'kanji', 'kaushik']


# ⁡⁢⁣⁣copy()⁡ ---> ⁡⁣⁢⁣create copy of a number⁡
num1  = [121,144,169,190,1343]
num2 = num1.copy()
print(num2) 
# [121, 144, 169, 190, 1343]


# ⁡⁢⁣⁣clear() ⁡---> ⁡⁣⁢⁣remove all element from list⁡
movie = ['yodha','baghi','solo','money']
movie.clear()
print(movie)

