
# a = int(input('enter the num : '))

# for i in range(1,11):
#     print(f'{a} X {i} = {a * i}')

# # print the n num of table
# for i in range(1,6):
#     print()
#     for j in range(1,11):
#         print(f'{i} X {j} = {i * j}')


# write a program to find factorial of all the num all int from the bellow list

# a = [2,17,18,20,8]

# out = []

# for i in a:
#     fact = 1
#     for j in range(i,0,-1):
#         fact = fact * j
#     out.append(fact)

# print(out)


# write a program to check whether given num is strong num or not
# ⁡⁢⁣⁢important!⁡

# a = int(input('enter the num : '))

# temp = a
# total = 0
# for i in str(temp):
#     digit = int(i)
#     fact = 1
#     for j in range(digit,0,-1):
#         fact = fact * j
#     total += fact

# if(total == a):
#     print(f'{a} is strong number!')
# else:
#     print(f'{a} is not strong number!')



# a = int(input('enter the num : '))

# strong = []

# tamp = a
# for i in range(1,a+1):
#     st = str(i)
#     total = 0
#     for j in st:
#         digit = int(j)
#         fact = 1
#         for k in range(digit,0,-1):
#             fact = fact * k
#         total += fact
#     if(total == i):
#         strong.append(total)
    
# print(strong)


# a = int(input('enter the num : '))

# total = 0
# for i in str(a):
#     fact = 1
#     digit = int(i)
#     for j in range(digit,0,-1):
#         fact = fact * j
#     total += fact
# if(total == a):
#     print('strong num')
# else:
#     print('not strong num')




# a = int(input('enter the number : '))

# strong = []

# for i in range(1,a+1):
#     total = 0
#     for j in str(i):
#         fact = 1
#         digit = int(j)
#         for k in range(digit,0,-1):
#             fact = fact * k
#         total += fact
#     if(total == i):
#         strong.append(total)

# print(strong)



# given num is arm string or not 

# sum of power of indevidual digit if it is equal to the number then the num is said to be arm strong num 
# ex 372,,,,153



# a = int(input('enter the num : '))

# st = str(a)
# sum = 0
# for i in st:
#     l = len(st)
#     for j in i:
#         digit = int(j)
#         sum = sum +  (digit ** l)
# if(sum == a):
#     print(f'{a} is arm strong num!')
# else:
#     print(f'{a} is not armstrong num!')




# wrt a program  to extract only wovwls from the given list

# a = ['program',1-5,True,'holiday',3+9j,14.5]

# wovel = []

# for i in a:
#     if(type(i) == str):
#         for j in i:
#             if(j in 'AEIOUaeiou'):
#                 wovel.append(j)
# print(wovel)



# write program to get the followibg out put

# a = ['program',1-5,True,'holiday',3+9j,14.5]

# dic = {}

# for i in a:
#     if(type(i) == str):
#         count = 0
#         for j in i:
#             if(j not in 'AEIOUaeiou'):
#                 count += 1
#         dic[i] = count
# print(dic)




# balance number :

# a = int(input('enter the num : '))

# new = str(a)
# l = len(new) // 2

# left = 0
# for i in range(0,l):
#     left = left + int(new[i])
# right = 0
# for j in range(l+1,len(new)):
#     right = right + int(new[j])
# if(left == right):
#     print('balance num!')
# else:
#     print('not a balance num')



# a = int(input('enter the num : '))

# new = str(a)
# mv = len(new) // 2

# left = 0
# for i in range(0,mv-1):
#     left += int(new[i])

# right = 0
# for j in range(mv+1,len(new)):
#     right += int(new[j])

# if(left == right):
#     print('balance number!')
# else:
#     print('not balance number!')



# wrp to print armstrong upto n 

# a = int(input('enter the num : '))

# total = []

# for i in range(1,a+1):
#     st = str(i)
#     l = len(st)
#     sum = 0
#     for j in st:
#         sum += int(j) ** l
#     if(i == sum):
#         total.append(sum)
# print(total)



# wrp to print num perfect num up to n

# perfect = []

# a = int(input('enter the num : '))

# for i in range(1,a+1):
#     conunt = 0
#     for j in range(1,i+1):
#         if(i % j == 0):
#             conunt += 1
#     if(conunt == 2):
#         perfect.append(i)
# print(perfect)
