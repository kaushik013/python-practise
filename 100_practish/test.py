


#//! 1. 

# input = {'E5' : 'Taj', 'E6' : 'Pallavi','T4' : 'Vishwa'}
# op = {'Taj' : 'E5' ,'Pallavi' : 'E6','Vishwa':'T4'}



# a = {'E5' : 'Taj', 'E6' : 'Pallavi','T4' : 'Vishwa'}

# dic = {}

# for i in a:
#     dic[a[i]] = i
# print(dic)



# write a python program  to count how many times each word occurs in a sentence 

# input = 'this is a test this is simple'
# output = {'this' : 2, 'is':2, 'a':1, 'test': 1, 'simple':1}


# a = 'this is a test this is simple'

# temp = a.split()

# dic = {}

# for i in temp:
#     if(i not in dic):
#         dic[i] = 1
#     else:
#         dic[i] = dic[i] + 1
# print(dic)




# 3 write a python program to print only those element from the list which are prime number

# input = [10,11,12,13,14,15]

# a = [10,11,12,13,14,15]

# for i in a:
#     for j in range(2,i):
#         if(i % j == 0):
#             break
#     else:
#         print(i)



# 4 wap to find the difference between product and sum of digit of a number 


# a = int(input('enter the num : '))

# sum = 0
# product_digits = 1


# for i in str(a):
#     dig = int(i)
#     sum += dig
#     product_digits *= dig

# print(f'the product and sum of digit between : {product_digits-sum}')




#! 5 wap to print sum of even-position and odd-position digits separately

# a = input('enter the num : ')

# even_sum = 0
# odd_sum = 0

# for i in range(0,len(a)):
#     if(i % 2 == 0):
#         even_sum += int(a[i])
#     else:
#         odd_sum += int(a[i])
# print(f'total even sum : {even_sum}')
# print(f'total odd sum : {odd_sum}')





# 6 
# input = {'V' : 10, 'VI' : 10, 'VII' : 40,'VIII' : 20,'IX' : 70,'X':80,'XI':40,'XII':20}
# output = {10:2, 40:2, 20:2, 70:1, 80:1}

# a = {'V' : 10, 'VI' : 10, 'VII' : 40,'VIII' : 20,'IX' : 70,'X':80,'XI':40,'XII':20}


# dic = {}

# for i in a:
#     if a[i] in dic:
#         dic[a[i]] += 1
#     else:
#         dic[a[i]] = 1
# print(dic)




# 7  
# s = ['python.py','pro1.html','pro3.py','google.com']


# l = []

# for i in s:
#     j = i.split('.')
#     l.append(j[-1])
# print(l)
