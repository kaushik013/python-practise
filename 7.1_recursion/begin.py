

# ⁡⁢⁣⁢sum of total element ⁡
#⁡⁣⁢⁣ using loop 🔂

# def sum_arr(arr):
#     total = 0
#     for i in arr:
#         total += i
#     return total

# print(sum_arr([1,2,3,4,5,6,7,8,9]))


# using recursion 🧠

# def sum_arr(arr):
#     if(not arr):
#         return  0
#     return arr[0] + sum_arr(arr[1::])

# print(sum_arr([1,2,3,4,5])) 


# ⁡⁢⁣⁢reverse the string⁡
# using loop 🔂
# def revers_str(str):
#     rev = ''
#     for i in str:
#         rev = i + rev
#     return rev

# print(revers_str('kaushik'))

# using recursion 🧠
# def rev_str(str):
#     if(len(str) <= 1):
#         return str
#     return  rev_str(str[1::]) + str[0]

# print(rev_str('hello'))


# ⁡⁢⁣⁢factorial ⁡
# usingn loop 

# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact * i
#     print(fact)

# factorial(5)


# using recursion

# def factorial(num):
#     if(num == 1 or num == 0):
#         return 1
#     return factorial(num - 1) * num

# print(factorial(5))



# ⁡⁢⁣⁢reverse digit ⁡
# using loop 

# def reverse_num(num):
#     total = 0
#     while num > 0:
#         fans = num % 10
#         total = total * 10 + fans
#         num //= 10
#     print(total)



# usinf recursion 
# def reverse_num(num, ex=0):
#     if(num == 0):
#         return ex
#     fans = num % 10
#     ex = ex * 10 + fans
#     return reverse_num(num // 10,ex) 

# print(reverse_num(1234))



# Write a recursive function to find the sum of digits of a number.


# def total_sum(num):
#     if(num == 0):
#         return 0
#     fans = num % 10
#     return fans + total_sum(num // 10)

# print(total_sum(123))


# Write a recursive function to count the total digits of a number.

# def total_num(num):
#     if(num == 0):
#         return 0
#     return 1 + total_num(num // 10) 

# print(total_num(123))


# Write a recursive function to calculate the factorial of a number.

# def factorial(fact):
#     if(fact == 0 or fact == 1):
#         return 1
#     return fact * factorial(fact - 1)

# print(factorial(5)) 


# Write a recursive function to calculate power of a number (a^b).

# def power_num(num,pwr):
#     if(pwr == 0):
#         return 1
#     return num * power_num(num, pwr - 1)
# print(power_num(2,3))
    
    