

# Q1.Write a program to print the following using while loop
# First 10 Even numbers
# Q2.First 10 Odd numbers
# Q3. First 10 Natural numbers
# Q4. First 10 Whole numbers
# Q5. Write a program to print first 10 integers and their squares using while loop.
# Q6. Write while loop statement to print the following series: 10, 20, 30 … … 300
# Q7. Write a while loop statement to print the following series 105, 98, 91 ………7.
# Q8. Write a program to print the first 10 natural number in reverse order using while loop.
# Q9. Write a program to print sum of first 10 Natural numbers.
# Q10. Write a program to print sum of first 10 Even numbers.





# Q1.Write a program to print the following using while loop

# a = 1
# count = 0
# while count < 10:
#     if(a % 2 == 0):
#         print(a)
#         count += 1
#     a += 1



# Q2.First 10 Odd numbers

# a = 1
# count = 0

# while count < 10:
#     if(a % 2 != 0):
#         print(a)
#         count += 1
#     a += 1



# Q3. First 10 Natural numbers

# a = 1
# i = 0

# while i < 10:
#     print(a)
#     a += 1
#     i += 1



# Q4. First 10 Whole numbers
# Whole Numbers = 0, 1, 2, 3, 4, 5, 6, …

# a = 0
# i = 0

# while i < 10:
#     print(a)
#     a += 1
#     i += 1




# Q5. Write a program to print first 10 integers and their squares using while loop.

# a = 1
# i = 0

# while i < 10:
#     print(a, '-->',a ** 2)
#     a += 1
#     i += 1



# Q6. Write while loop statement to print the following series: 10, 20, 30 … … 300

# a = 10 
# i = 0

# while i < 300:
#     print(a)
#     a += 10
#     i += 10



# Q7. Write a while loop statement to print the following series 105, 98, 91 ………7.

# a = 105
# i  = 0

# while i < a:
#     print(a)
#     a -= 7



# Q8. Write a program to print the first 10 natural number in reverse order using while loop.

# a = 10
# i = 0

# while i < a:
#     print(a)
#     a -= 1




# Q9. Write a program to print sum of first 10 Natural numbers.

# a = 1
# sum = 0

# while a <= 10:
#     sum += a
#     a +=1
# print('total sum : ',sum)




# Q10. Write a program to print sum of first 10 Even numbers.


# count = 0
# num = 1
# total = 0

# while count < 10:     
#     if num % 2 == 0:
#         total += num
#         count += 1
#     num += 1
# print("sum is : ", total)





    

# Q11. Write a program to print table of a number entered from the user.
# Q12. Write a program to print all even numbers that falls between two numbers (exclusive
# both numbers) entered from the user using while loop.
# Q13. Write a program to check whether a number is prime or not using while loop.
# Q14. Write a program to find the sum of the digits of a number accepted from the user.
# Q15. Write a program to find the product of the digits of a number accepted from the user.
# Q16. Write a program to reverse the number accepted from user using while loop.
# Q17. Write a program to display the number names of the digits of a number entered by
# user, for example if the number is 231 then output should be Two Three One
# Q18. Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop.



# Q11. Write a program to print table of a number entered from the user.

# a = int(input('enter the number : '))

# i = 1

# while i <= 10:
#     print(f'{a} X {i} = {a * i}')
#     i += 1



# Q12. Write a program to print all even numbers that falls between two numbers (exclusive
# both numbers) entered from the user using while loop.


# a = 99
# i = 0

# while a > i:
#     if(a % 2 == 0):
#         print(a)
#     a -= 1



# Q13. Write a program to check whether a number is prime or not using while loop.



# a = int(input('enter the num : '))
# count = 0
# i = 1

# while i <= a:
#     if(a % i == 0):
#         count += 1
#     i += 1

# if(count == 2):
#     print(f'{a} is prime number!')
# else:
#     print(f'{a} is not prime number!')



# Q14. Write a program to find the sum of the digits of a number accepted from the user.


# a = int(input('enter the number : '))

# sum = 0

# while a > 0:
#     b = a % 10
#     sum += b
#     a //= 10

# print(sum)




# Q15. Write a program to find the product of the digits of a number accepted from the user.
# 2 × 3 × 4 = 24 example

# a = int(input('enter the number : '))

# multi = 1

# while a > 0:
#     b = a % 10
#     multi *= b
#     a //= 10
# print(multi)



# Q16. Write a program to reverse the number accepted from user using while loop.

# a = int(input('enter the numbwr : '))

# rev = 0

# while a > 0:
#     b = a % 10
#     rev = rev * 10 + b
#     a //= 10

# print(rev)




# Q17. Write a program to display the number names of the digits of a number entered by
# user, for example if the number is 231 then output should be Two Three One

# a = int(input('enter the number : '))

# num = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}

# final = ''

# while a > 0:
#     b = a % 10
#     final = num[b] + ' ' + final
#     a //= 10

# print(final)





# Q18. Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop.

# n = int(input('enter the number : '))

# a = 0
# b = 1
# i = 0

# while i <= n:
#     print(a)
#     c = a + b
#     a,b = b,c
#     i += 1



