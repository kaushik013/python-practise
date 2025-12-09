
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