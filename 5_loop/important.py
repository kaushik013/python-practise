
# 1.Write a program to extract all the lower case character from the given string only if its ascii value 
# is even 

# 2..Write a program to find the length of the longest word  from the string

# 3. Write a program to display all the numbers which are divisible by 13 but not by 
# between 100 and 500.




# 1.⁡⁢⁣⁢Write a program to extract all the lower case character from the give⁡n⁡ 

# a = input('enter the string  : ')

# temp = ''

# for i in range(len(a)):
#     if(a[i] >= 'a' and a[i] <= 'z'):
#         if(ord(a[i]) % 2 == 0):
#             temp += a[i]
# print(temp)




# 2..‍‍‍Write a program to find the length of the longest word  from the string


# a = input('enter the sreing : ')


# words = a.split()

# empt = ''
# final = 0

# for i in range(0,len(words)):
#     if(len(words[i]) >= final):
#         final = len(words[i])
#         empt = words[i]

# print(f'the longest word length is : "{final}" and word is "{empt}" ')


# 3. Write a program to display all the numbers which are divisible by 13 but not by 
# between 100 and 500.


# for i in range(1,1000):
#     if(i % 13 == 0):
#         if(i >= 100 and i <= 500):
#             continue
#         else:
#             print(i)



# reverse the string 

# a = input('enter the text : ')

# reverse = ''

# for i in range(len(a)-1,-1,-1):
#     reverse += a[i]
# print(reverse)



# ⁡⁢⁣⁢extract wovel⁡
# a = input('enter the text : ')

# extWovl = ''

# for i in a:
#     if(i in 'AEIOUaeiou'):
#         extWovl += i
# print(extWovl)



# ⁡⁢⁣⁢pallindrom or not ⁡

# a = input('enter the string : ')

# new = ''

# for i in a:
#     new = i + new

# if(new == a):
#     print(f'{new} is pallindrom')
# else:
#     print('not pallindrom')



# a = int(input('enter the num : '))


# total = ''
# for i in str(a):
#     total = i + total
# total = int(total)
# print(total,type(total))


#  ⁡⁢⁣⁢pallindrom or not ⁡
# if(a == total):
#     print(f'{total} pllindrom')
# else:
#     print(f'{total} not pallindrom')


# a = [True,3.4,9,8,'Python']

# our = []

# for i in a:
#     if(type(i) == int):
#         our.append(i)
# print(our)


# ⁡⁢⁣⁢given collection is homogenous or not ⁡

# a = eval(input('enter the value : '))

# check = type(a[0])

# total = 0
# for i in a:
#     if(type(i) != check):
#         total = total + 1 

# if(total == 0):    
#     print('homogenous!')
# else:
#     print('hetrogenous!')



# a  = int(input('enter the num : '))

# b = []

# for i in range(1,a+1,1):
#     if(a % i == 0):
#         b.append(i)
# print(b)



#  ⁡⁢⁣⁢perfect number or not ⁡
# a = int(input('enter the num : '))

# b = 0

# for i in range(1,a,1):
#     if(a % i == 0):
#         b += i

# if(a == b):
#     print('perfect number!')
# else:
#     print('not perfect number!')



# ⁡⁢⁣⁢upto n total perfect number ⁡
# a = int(input('enter the num : '))

# total = []

# for i in range(1,a+1):
#     sum = 0
#     for j in range(1,i):
#         if(i % j == 0):
#             sum += j
#     if(sum == i):
#         total.append(i)
# print(total)



# ⁡⁢⁣⁢prime num or not ⁡

# a = int(input('enter the num : '))


# counter = 0
# for i in range(1,a+1,1):
#     if(a % i == 0):
#         counter += 1
    
# if(counter == 2):
#     print('prime number!')
# else:
#     print('not prime number!')


# or 


# a = int(input('enter the num : '))

# counter = 0

# for i in range(2,a):
#     if(a % i == 0):
#         counter += 1

# if(counter == 0):
#     print('prime number!')
# else:
#     print('not prime number!')


# ⁡⁢⁣⁢n num of prime number ⁡

# a = int(input('enter the num : '))


# empt = []

# for i in range(1,a+1):
#     counter = 0
#     for j in range(1,i+1):
#         if(i % j == 0):
#             counter += 1
#     if(counter == 2):
#         empt.append(j)

# print(empt)



# ⁡⁢⁣⁢factorial⁡

# a = int(input('enter the num : '))

# fact = 1

# for i in range(1,a+1):
#     fact = fact * i

# print(f'the factorial of {a} is : {fact}')


# ⁡⁢⁣⁢n number of factorial ⁡
# a = int(input('enter the num : '))

# factorial = []

# for i in range(1,a+1):
#     fact = 1
#     for j in range(1,i+1):
#         fact = fact * j
#     factorial.append(fact)


# print(factorial)        



# ⁡⁢⁣⁢important⁡
# a = [1,2,10,15,1,45,10]

# new = []

# for i in a:
#     if(i not in new):
#         new.append(i)

# print(new)


# ⁡⁢⁣⁢important⁡

# a = ['kaushik',12,11,14,12,12,True,False,12.11]

# new = []

# for i in a:
#     if(i not in new and type(i) == int):
#         new.append(i)

# print(new)



# a = 'pYThON#1%'

# output = 'YTONph#%1'

# upper = '' 
# lower = '' 
# digit = '' 
# specil = ''

# for i in a:
#     if(i >= 'A' and i <= 'Z'):
#         upper += i
#     elif(i >= 'a' and i <= 'z'):
#         lower += i
#     elif(i >= '0' and i <= '9'):
#         digit += i
#     else:
#         specil += i

# new = upper + lower + specil + digit

# print(new)



# count char,  digit, special
# a = 'pYThON5#1%'

# char = 0
# digit = 0
# specil = 0

# for i in a:
#     if(i >= 'A' and i <= 'Z' or i >= 'a' and i <= 'z'):
#         char += 1
#     elif(i >= '0' and i <= '9'):
#         digit += 1
#     else:
#         specil += 1

# print(char)
# print(digit)
# print(specil)


# ⁡⁢⁣⁢important 
# var = [key] = Value

# a = ['Pythin','hii','holiday','byee']

# output = {'Pythin': 6, 'hii': 3, 'holiday': 7, 'byee': 4}

# dict_my = {}

# for i in a:
#     dict_my[i] = len(i)
# print(dict_my)




# if string is even reverse the string else count the len 

# a = ['Pythin','hii','holiday','byee']

# # {'Pythin': 'nihtyP', 'hii': 3, 'holiday': 7, 'byee': 'eeyb'}

# dict_my = {}

# for i in a:
#     if(len(i) % 2 == 0):
#         dict_my[i] = i[::-1]
#     else:
#         dict_my[i] = len(i)

# print(dict_my)




#output  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# dic = {}

# for i in range(1,11):
#     dic[i] = i * i

# print(dic)




# output = {2: 4, 3: 27, 4: 16, 5: 125, 6: 36, 7: 343, 8: 64, 9: 729, 10: 100}

# dic = {}

# for i in range(2,10+1):
#     if(i%2 == 0):
#         dic[i] = i * i
#     else:
#         dic[i] = i ** 3

# print(dic)



#output = {'python': 6, 'is': 2, 'easy': 4}


# a = 'python is easy'

# final = a.split()

# dic = {}

# for i in final:
#     dic[i] = len(i)

# print(dic)

# {'python': 6, 'is': 2, 'easy': 4}





# 1.Input : (12,3.4,'hello',2+3j,'python','bye',False)
#  Output : {'hello': 5, 'python': 6,'bye':3} 


# a =  (12,3.4,'hello',2+3j,'python','bye',False)


# dic = {}

# for i in a:
#     if(type(i) == str):
#         dic[i] = len(i)
# print(dic)




# a =  [12,3.4,'hello',2+3j,'python','bye',False]
# #   Output : {'hello': 'ho', 'python': 'pn','bye':'be'} 

# dic = {}

# for i in a:
#     if(type(i) == str):
#         dic[i] = i[0]+i[-1]

# print(dic)



# 3. Input : 'my name is yash patel'
#    Output :{'my':2 , 'name': 4, 'yash':4 ,'patel':5}

# a = 'my name is yash patel'
# dic = {}

# lis = a.split()

# for i in lis:
#     dic[i] = len(i)

# print(dic)



# 4. Write a program to replace string with underscore in string

# a = input('enter the str : ')

# new = ''
# for i in a:
#     if(i == ''):
#         i = '_'
#         new += i 
#     new += i

# print(new)




# output =  {'a': 2, 'b': 1, 'c': 2, 'd': 1, 'e': 2}
# a = 'aabcdece'

# dic = {}

# for i in a:
#     if(i not in dic):
#         dic[i] = 1
#     else:
#         dic[i] = dic[i] + 1
    
# print(dic)




# a = {'python' : 2, 'is' : 2, 'easy' :  1, 'dynamically' : 1, 'typed' : 1}

# a = 'python is easy python is dynamically typed'

# final = a.split()

# dic = {}

# for i in final:
#     if(i not in dic):
#         dic[i] = 1
#     else:
#         dic[i] = dic[i] + 1

# print(dic)




# a = 'aaabbcccdd'

# dic = {}

# for i in a:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1

# print(dic)


# 1.Write a Python program to group numbers by their remainder when divided by 3.
# Input list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: {0: [3, 6, 9], 1: [1, 4, 7], 2: [2, 5, 8]

a =  [1, 2, 3, 4, 5, 6, 7, 8, 9]

dic = {}

# for i in a:
#     if(i % 3 == 0):
#         dic[0] = [i]
#     elif(i % 3 == 1):
#         dic[1] = [i]
#     else:
#         dic[2] = [i]

# print(dic)



# for i in a:
#     reminder = i % 3
#     if(reminder not in dic):
#         dic[reminder] = []
#     else: 
#         dic[reminder].append(i)
# print(dic)



# 2.Write a python program to count how many numbers are greater than 50 and count how many numbers are odd numbers.
# a=[10, 55, 42, 17, 58]
# Output: Numbers greater than 50 : 2
#                 Even numbers : 3

# a = [10, 55, 42, 17, 58]

# grater_50 = 0
# even = 0

# for i in a:
#     if(i > 50):
#         grater_50 += 1
#     if(i % 2 == 0):
#         even = even + 1

# print(f'Numbers greater than 50 {grater_50}')
# print(odd)







# 3.Write a python program to find the highest marks and how many students got them.
# marks = {'Anu': 85, 'Raj': 90, 'Meena': 92, 'Kiran': 92}
# Output:
# Highest Marks : 92
# Students : ['Meena', 'Kiran']


# marks = {'Anu': 85, 'Raj': 90, 'Meena': 92, 'Kiran': 92}

# Highest_Marks =  0
# Students = []

# for i in marks:
#     if(marks[i] > Highest_Marks):
#         Highest_Marks = marks[i]

# for i in marks:

#     if(marks[i] == Highest_Marks):
#         Students.append(i)


# print(Highest_Marks)
# print(Students)














































