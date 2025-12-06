

# Write a recursive function to find the sum of digits of a number.

# Input:  523
# Output: 10   (5 + 2 + 3)

# def sum_digit(num):
#     if(num == 0):
#         return 0
#     fans = num % 10
#     sans = num // 10
#     return fans + sum_digit(sans)

# print(sum_digit(541))

# or 

# def sum_digit(num):
#     if(num == 0):
#         return 0
#     fans = num % 10
#     return fans + sum_digit(num // 10)

# print(sum_digit(541))



# Write a recursive function to count how many digits are in a number.

# def count_digit(num):
#     if(num == 0):
#         return 0
#     sum = num // 10
#     return 1 + count_digit(sum)

# print(count_digit(144223))



# Write a recursive function to calculate the power:

# def calculate_pwr(num,how):
#     if(how == 0):
#         return 1
#     total = num * calculate_pwr(num,how - 1)
#     return total

# print(calculate_pwr(2,2))


# Write a recursive function to reverse a number.

# a = 1234

# sum = 0

# while a > 0:
#     first = a % 10
#     sum = sum * 10 + first
#     a //= 10

# print(sum)



