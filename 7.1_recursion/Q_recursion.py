
#! function to find factorial a given number using recursion

# def factorial(n,fact = 1):
#     if(n <= 0):
#         return fact
#     fact *= n
#     return factorial(n - 1,fact)
# print(factorial(5))

# ! while loop
# a = 5
# fact = 1

# while a > 0:
#     fact *= a
#     a -= 1
# print(fact)



# a = 1

# while a <= 20 :
#     if(a % 2 == 0):
#         print(a)
#     a += 1


# def even(n):
#     if(n > 20):
#         return 
#     if(n % 2 == 0):
#         print(n)
#     return even(n + 1)
# even(1)


# ! while loop
# a = int(input('entrr the num : '))
# i = 1
# b = 0
# c = 1
# while i <= a:
#     print(b)
#     d = b + c
#     b,c = c,d
#     i += 1

#! recursion
# def fibonacci(n = 10, k = 1, a = 0, b = 1):
#     if(k > n):
#         return
#     print(a)
#     return fibonacci(n,k + 1, b, a + b)

# fibonacci()


# n=13
# i=2
# while i<n:
#     if n%i==0:
#         print('not prime')
#         br
#     i+=1
# else:
#     print('prime')



# def prime(n,i=2):
#     if i==n:
#         return 'prime'
#     if n%i==0:
#         return('not prime')

#     return prime(n,i+1)

# print(prime(11))

# a = int(input('enter the num : '))

# for i in range(1,a+1):
#     for j in range(2,i):
#         if(i % j == 0):
#             break
#     else:
#         print(i)


# a = int(input('enter the num : '))

# for i in range(1,a+1):
#     st = str(i)
#     power = len(st)
#     count = 0
#     for j in st:
#         count += int(j) ** power
#     if(count == i):
#         print(i)

# a = int(input('enter the num : '))

# for i in range(1,a+1):
#     st = str(i)
#     pwr = len(st)
#     count = 0
#     for j in st:
#         count += int(j) ** pwr
#     if(count == i):
#         print(i)


# a = int(input('enter the num : '))

# for i in range(2,a+1):
#     for j in range(2,i):
#         if(i%j == 0):
#             break
#     else:
#         print(i)


# # ! strong num
# a = int(input('enter the num : '))

# fact = 0
# for i in str(a):
#     count = 1
#     k = int(i)
#     for j in range(1,k+1):
#         count *= j
#     fact += count
# if(fact == a):
#     print('strong num')
# else:
#     print('not strong num')


# ! strong num
# a = int(input('enter the num : '))

# for i in range(1,a+1):
#     st = str(i)
#     total = 0
#     for j in st:
#         fact = 1
#         n = int(j)
#         for k in range(1,n+1):
#             fact *= k
#         total += fact
#     if(total == i):
#         print(i)


# ! perfect num

# a = int(input('enter the num : '))

# count = 0
# for i in range(1,a):
#     if(a % i == 0):
#         count += i
# if(count == a):
#     print('perfect num')
# else:
#     print('not perfect')

# # ! perfect num upto n

# a = int(input('enter the num : '))

# for i in range(1,a+1):
#     count = 0
#     for j in range(1,i):
#         if(i % j == 0):
#             count += j
#     if(count == i):
#         print(i)



# def fibonacci(n,i=1,a=0,b=1):
#     if(i>n):
#         return
#     print(a)
#     return fibonacci(n,i+1,b,a+b)
# fibonacci(10)


# n = 5

# temp = 1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(temp,end=' ')
#         temp+= 1
#     temp -= 1
#     print()

# ! important
# 1 
# 1 2 
# 2 3 4 
# 4 5 6 7 
# 7 8 9 10 11 