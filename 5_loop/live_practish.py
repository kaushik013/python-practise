

# 1️⃣ ⁡⁢⁣⁣Print numbers from 1 to 20⁡

# for i in range(1,21,1):
#     print(i)

# 2️⃣ ⁡⁢⁣⁣Print even numbers from 1 to 100⁡

# for i in range(1,101,1):
#     if(i%2 == 0):
#         print(i)

# 3️⃣⁡⁢⁢⁣ ⁡⁢⁣⁣Print odd numbers from 1 to 50⁡

# for i in range(1,51):
#     if(i%2 != 0):
#         print(i)

# 4️⃣ ⁡⁢⁣⁣Print reverse numbers from 50 to 1⁡

# for i in range(50,0,-1):
#     print(i)

# 5️⃣ ⁡⁢⁣⁣Print table of any number (take input)⁡

# a = int(input('enter the number : '))

# for i in range(1,11):
#     print(f'{a} X {i} = {a*i}')




# b = int(input('enter the number : '))
# n = 20

# while n < 30:
#     print(f'{b} X {n-19} = {b*(n-19)}')
#     n += 1


# 6️⃣ ⁡⁢⁣⁣Find sum of numbers from 1 to n⁡

# a = int(input('enter the number : '))
# sum = 0
# for i in range(1,a+1):
#     sum += i
# print(sum)


# 7️⃣ ⁡⁢⁣⁣Find sum of even numbers from 1 to n⁡

# a = int(input('enter the number : '))
# sum = 0
# for i in range(1, a+1):
#     if(i % 2 == 0):
#         sum += i
# print(sum)


# 8️⃣ ⁡⁢⁣⁣Find sum of odd numbers from 1 to n⁡

# b = int(input('enter the number : '))
# sum = 0
# for i in range(1, b+1):
#     if(i % 2 != 0):
#         sum += i
# print(sum)


# 9️⃣ ⁡⁢⁣⁣Find factorial of a number⁡

# a = int(input('enter the number : '))
# fact = 1
# for i in range(1,a+1):
#     fact *= i
# print(fact)

# 🔟⁡⁢⁣⁣ Count how many numbers between 1 to n are divisible by 5⁡

# a = int(input('enter the number : '))
# count = 0
# li = []
# for i in range(1, a+1):
#     if(i%5 == 0):
#         count += 1
#         li.append(i)

# print(count)
# print(li)

# 1️⃣1️⃣ ⁡⁢⁣⁣Reverse a string⁡

# a = input('enter the name : ')
# str = ''
# for i in range(len(a)-1,-1,-1):
#     str += a[i]
# print(str)



# ⁡⁢⁣⁣prime number⁡

# a = int(input('enter number : '))

# b = []
# for i in range(1,a+1):
#     count = 0
#     for j in range(1,i+1):
#         if(i%j == 0):
#             count += 1
#     if(count == 2):
#         b.append(i)
# print(b)



# ⁡⁢⁣⁣perfect number 1 to 100 ⁡
# a = int(input('enter the num : '))
# lis = []

# for i in range(1,a+1):
#     sum = 0
#     for j in range(1,i):
#         if(i%j == 0):
#             sum += j
#     if(sum == i):
#         lis.append(i)
# print(lis)



# ⁡⁢⁣⁣armstrong number or not⁡ 
# a = int(input('enter the number : '))


# temparary = a
# sum = 0

# while temparary > 0:
#     reminder = temparary % 10
#     sum = sum + reminder ** 3
#     temparary = temparary // 10
# if(a == sum):
#     print('armstrong number!')
# else:
#     print('not armstrong number!')



#⁡⁢⁣⁣ reverse string⁡
# n = input('enter the name : ')
# new = ''

# for i in range(len(n)-1,-1,-1):
#     new += n[i]

# print(new)
