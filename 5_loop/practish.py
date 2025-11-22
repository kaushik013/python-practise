

# ⁡⁢⁣⁣for loop in python ⁡


# for i in range(1,21,1):
#     print(i)

# for i in range(20,0,-1):
#     print(i)


# a = int(input('enter number : '))

# for i in range(1,11,1):
#     print(f'{a} X {i} = {a*i}')

# a = 'Kaushik'

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)


# ⁡⁢⁣⁣break statment⁡
# name = 'Chariya kaushik'

# for i in name:
#     if(i == 'k'):
#         break
#     print(i)

# ⁡⁢⁣⁣continue statment⁡
# for i in range(1,10,1):
#     if(i == 5):
#         continue
#     print(i)



# for i in range(1,10,1):
#     if(i == 12):
#         print('break statment is  execute!')
#         break
#     print(i)
# else:
#     print('break statment is not executed!')


# ⁡⁢⁣⁣natural number⁡
# n = int(input('enter number : '))

# for i in range(n+1):
#     print(i)


# ⁡⁢⁣⁣reverse natural number⁡
# n = int(input('enter natural num : '))

# for i in range(n,0,-1):
#     print(i)


# ⁡⁢⁣⁣table⁡

# n = int(input('enter number : '))

# for i in range(1,11,1):
#     print(f'{n} X {i} = {i*n}')


# ⁡⁢⁣⁣natural sum of n ⁡
# n = int(input('enter number : '))

# sum = 0
# for i in range(1,n+1):
#     print(i)
#     sum += i
# print('total : ', sum)


#⁡⁢⁣⁣ factorial⁡
# n = int(input('enter number : '))
# fact = 1
# for i in range(1,n+1,1):
#     fact *= i
# print(fact)


# ⁡⁢⁣⁣sum of 10 number⁡

# sum = 0

# for i in range(1,11,1):
#     sum += i
# print(sum)


# fact = 1
# n = int(input('enter number : '))
# for i in range(1,n+1,1):
#     fact *= i
# print(fact)



# ⁡⁢⁣⁣print sum of even or odd ⁡
# even = 0
# odd = 0

# for i in range(1,21,1):
#     if(i%2 == 0):
#         even += i
#     else:
#         odd += i
# print(even)
# print(odd)




# ⁡⁢⁣⁣all factor number :⁡

# n = int(input('enter the number : '))

# for i in range(1,n+1):
#     if(n%i == 0):      
#         print(f'factor is {i}')
# print(f'all factor of = {n}')


# ⁡⁢⁣⁣perfect number or not ⁡

# n = int(input('enter the number : '))
# sum = 0
# for i in range(1,n):
#     if(n%i == 0):
#         sum += i

# if(sum == n):
#     print(f'{n} is perfect number!')
# else:
#     print(f'{n} is not perfect number!')


# ⁡⁢⁣⁣number is prime or not ⁡

n = int(input('enter the number : '))
count = 0
for i in range(1,n+1):
    if(n%i == 0):
        count += 1

if(count == 2):
    print('prime number!')
else:
    print('not prime number!')


# n number of prime numbers

# a = int(input('enter the number: '))
# prime = []
# for i in range(1, a+1):
#     count = 0
#     for j in range(1,i+1):
#         if(i%j == 0):
#             count += 1
#     if(count == 2):
#         prime.append(i)
# print(prime)

