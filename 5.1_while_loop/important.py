

#⁡⁢⁣⁢ important ⁡

# input this and output that like pYtHon@12

# a = 'PyThON@12'
# i = 0
# final = ''
# while i < len(a):
#     upp = chr(ord(a[i]) + 32)
#     low = chr(ord(a[i]) - 32)
#     if('A' <= a[i] <= 'Z'):
#         final += upp
#     elif('a' <= a[i] <= 'z'):
#         final += low
#     else:
#         final += a[i]
#     i +=1
# print(final)



# c⁡⁢⁣⁢heck character upper lower digit or special⁡
# a = 'PyTHoN@5!9'

# i = 0 
# uppercase = 0
# lowercase = 0
# digit = 0
# special = 0

# while i < len(a):
#     if a[i] >= 'A' and a[i] <= 'Z':
#         uppercase += 1

#     elif a[i] >= 'a' and a[i] <= 'z':
#         lowercase += 1

#     elif  '0' >= a[i]  and a[i] <= '9':
#         digit += 1

#     else:
#         special += 1

#     i += 1

# print("Uppercase =", uppercase)
# print("Lowercase =", lowercase)
# print("Digit =", digit)
# print("Special =", special)



# Fibonacci Series (Simple Explanation)
# n = int(input('enter the num : '))

# i = 1
# a = 0
# b = 1

# while i <= 10:
#     c = a + b
#     print(c)
#     a,b = b,c
#     i += 1



# ⁡⁢⁣⁢total of fibonacci ⁡
# n = int(input('enter the num : '))

# i = 1
# a  = 0
# b = 1
# total = 0
# while i <= n:
#     c = a + b
#     print(c)
#     total += c
#     a,b = b,c
#     i += 1
# print(f'total is : {total}')



# ⁡⁢⁣⁢factorial⁡
# a = int(input('enter the number : '))

# fact = 1
# i = 1

# while i <= a:
#     fact *= i
#     i += 1
# print(fact)


# ⁡⁢⁣⁢important⁡
# a = input('enter the nummber : ')

# upper = 0
# lower = 0
# digit = 0
# special = 0

# total = {}

# i = 0
# while i < len(a):
#     if(a[i] >= 'A' and a[i] <= 'Z'):
#         upper += 1
#         if(a[i] in total):    
#             total[a[i]] += 1
#         else:
#             total[a[i]] = 1   

#     elif(a[i] >= 'a' and a[i] <= 'z'):
#         lower += 1
#         if(a[i] in total):    
#             total[a[i]] += 1
#         else:
#             total[a[i]] = 1

#     elif(a[i] >= '0' and a[i] <= '9'):
#         digit += 1
#         if(a[i] in total):
#             total[a[i]] +=  1
#         else:
#             total[a[i]] = 1
#     else:
#         special += 1
#         if(a[i] in total):
#             total[a[i]] += 1
#         else:
#             total[a[i]] = 1
#     i += 1

# print(f'total upper : {upper}')
# print(f'total lower : {lower}')
# print(f'total digit : {digit}')
# print(f'total special : {special}')

# for i in total.items():
#     print(i)


# a = 'PyThoN2023@!#'

# upper = 0
# lower = 0
# digit = 0
# specil = 0

# i = 0
# while i < len(a):
#     if(ord(a[i]) >= 65 and ord(a[i]) <= 90):
#         upper += 1
#     elif(ord(a[i]) >= 97 and ord(a[i]) <= 122):
#         lower += 1
#     elif(ord(a[i]) >= 48 and ord(a[i]) <= 57):
#         digit += 1
#     else:
#         specil += 1 
#     i += 1


# print(f'total upper : {upper}')
# print(f'total lower : {lower}')
# print(f'total digit : {digit}')
# print(f'total special : {specil}')



# reverse the number
# a = int(input('enter the number : '))

# total = 0
# while a > 0:
#     c = a % 10
#     total = total * 10 + c
#     a //= 10
# print(total)



# pallind rom or not 
# a = int(input('enter the number : '))

# temp = a

# total = 0
# while temp > 0:
#     c = temp % 10
#     total = total * 10 + c
#     temp //= 10
# print(total)

# if(a == total):
#     print('pallindrom')
# else:
#     print('not pallindrom')




# 1.Write a program to find the sum of digits of a number

# 2.Write a program to print the sum of odd numbers  and even numbers separately between the limits given 
# by user

# 3. Write a program to print the following sequence for n terms
# 1 4 9 16 25 ...... n terms

# 4. Write a program to print the sum of n terms of the following series 
# 1 + 8 + 27+ .... n terms

# 5.Write a program to print the factors of a given number




# 1.Write a program to find the sum of digits of a number

# a = int(input('Enter the number : '))

# sum = 0
# while a > 0:
#     c = a % 10 
#     sum += c
#     a //= 10
# print(sum)




# 2.Write a program to print the sum of odd numbers  and even numbers separately between the limits given 
# by user

# a = int(input('enter the number : '))

# even = 0
# odd = 0

# i = 1
# while i <= a:
#     if(i % 2 == 0):
#         even += i
#     else:
#         odd += i
#     i += 1
# print(f'sum of even number : {even} ')
# print(f'sum of odd number : {odd} ')




# 3. Write a program to print the following sequence for n terms
# 1 4 9 16 25 ...... n terms

# a = int(input('enter the number : '))
 
# i = 0
# while i <= a:
#     print(i * i)
#     i += 1




# 4. Write a program to print the sum of n terms of the following series 
# 1 + 8 + 27+ .... n terms


# a = int(input('enter the number : '))

# i = 1
# sum = 1
# while i <= a:
#     c = i * i * i
#     print(c)
#     sum += c 
#     i += 1
# print(f'total sum is : {sum}')




# 5.Write a program to print the factors of a given number
 
# a = 5
# fact = 1
# i = 1
# while a >= i:
#     fact = fact * a
#     a -= 1
# print(fact)
