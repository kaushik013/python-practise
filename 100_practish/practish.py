
# a = int(input('enter the num : '))

# if(a > 0):
#     print('positive num!')
# elif(a < 0):
#     print('nagative num!')
# else:
#     print('Zero!')


# for i in range(1,51):
#     for j in range(2,i):
#         if(i % j == 0):
#             break
#     else:
#         print(i)


# a =12345
# rev = 0

# while a > 0:
#     b = a % 10
#     rev = rev * 10 + b
#     a //= 10
# print(rev)


# def arm_strong(n):
#     new = 0
#     for i in n:
#         new += int(i) ** 3
#     if new == int(n):
#         print('armstrong')
#     else:
#         print('not armstrong')

# a = input('enter the num : ')
# arm_strong(a)


# def factorial(n,fact = 1):
#     if(n <= 0):
#         return fact
#     fact *= n
#     return factorial(n - 1,fact)

# print(factorial(5))



# a = 907060
# count = 0

# while a > 0:
#     count += 1
#     a //= 10
# print(count)


# a = 1221

# temp = a

# pallind = 0
# while temp > 0:
#     b = temp % 10
#     pallind = pallind * 10 + b
#     temp //= 10

# if(pallind == a):
#     print('pallindrom num!')
# else:
#     print('not palindrom num!')


def prime(n, k=2):
    if n <= 1:
        return "not prime"
    if k * k > n:
        return "prime"
    if n % k == 0:
        return "not prime"
    return prime(n, k + 1)

a = int(input("enter the num : "))
print(prime(a))
