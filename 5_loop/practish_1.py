
# ⁡⁢⁣⁢qus 1.⁡
# ⁡⁣⁣⁢Write a Python program to find the sum of all numbers from 1 to N using a for loop.
# Example:
# Input: 5  
# Output: 15   # (1 + 2 + 3 + 4 + 5)⁡

j = 1
sum = 0
while j <= 15:
    sum += j  # adds j to sum each time
    j += 1    # increments j
print(sum)
# 120


#⁡⁢⁣⁢ qus 2⁡.

# ⁡⁣⁣⁢Write a Python program to print the multiplication table of a number using a for loop.
# Example:
# Input: 5
#   
# Output:
# 5 x 1 = 5  
# 5 x 2 = 10  
# 5 x 3 = 15  
# ...  
# 5 x 10 = 50⁡

i = 10
for j in range(1,11,1):
    print(f'{i} X {j} = {j * i}')


# ⁡⁣⁣⁢Write a Python program to count how many digits are in a given number using a while loop.
# Example:
# Input: 12345  
# Output: 5⁡


num = 123456
i = 0

while num > 0:
    num = num // 10
    i += 1
print(i)

