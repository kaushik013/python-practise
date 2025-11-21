

# ⁡⁣⁣⁢list sorted or not ⁡

lists = [1,2,3,3,4,2,5,6,6]


for i in range(len(lists)-1):
    if(lists[i] <= lists[i + 1]):
        continue
    else:
        print('not sorted!')
        break
else:
    print('sorted list')




# ⁡⁣⁣⁢ 1.⁡ ⁡⁣⁣⁢Find Average Marks⁡
# ⁡⁣⁣⁢Question: Given a list of marks, find the average marks of all students⁡.
# ⁡⁢⁣⁣Hint: Use sum(marks) and len(marks) → average = total ÷ number of elements⁡


mark = [99,98,87,98,87,67,78]

sum = 0
for i in range(len(mark)):
    sum = sum + mark[i]
    print(f'total sum is : {sum}')
    print(f'avarage is {sum / len(mark):.2f}%')


# 2.⁡⁣⁣⁢ Find Largest and Second Largest Number
# Question: Find the largest and second largest number in a list.⁡
# ⁡⁢⁣⁣Hint: Use sort() and access [-1] (largest) and [-2] (second largest).⁡

# ⁡⁣⁢⁣using method⁡
num = [12,42,54,56,34,45,43,2,23,4,64]
num.sort()
print(f'largest num is : {num[-1]}')
print(f'second largest num is : {num[-2]}')



# ⁡⁣⁢⁣using loop⁡ (⁡⁢⁣⁢tough⁡)

large = num[i]
sec_large = num[i]

for i in range(len(num)):
    if(num[i] > large):
        sec_large = large
        large = num[i]
print(f'large num = {large}')
print(f'second large num = {sec_large}')


# ⁡⁣⁣⁢3. Remove Duplicates
# Question: Remove duplicates from a list and print only unique elements and assending order .⁡
# ⁡⁢⁣⁣Hint: Convert list to set() → removes duplicates → then convert back to list()⁡

score = [11,23,43,11,34,33,5,32,43,23]

set_item = set(score)

new_score  = list(set_item)
new_score.sort()
print(new_score)


# ⁡⁣⁣⁢Names Starting With ‘A’
# Question: Create a list of names and print only those starting with the letter 'A'.⁡
# ⁡⁢⁣⁣Hint: Use a for loop with condition if name.startswith('A'):.⁡

name = ['kaushik','kajal','ashmita','arijit','yas','arti']

for i in name:
    if(i.startswith('a')):
        print(i)
    else:
        continue


# ⁡⁣⁣⁢5. Sum of Even Numbers
# Question: Create a list of integers and print the sum of all even numbers only.⁡
# ⁡⁢⁣⁣Hint: Use a loop and condition if num % 2 == 0: → add to total.

even = [13,12,15,6]
sum = 0
for i in even:
    if(i % 2 == 0):
        sum = sum + i
    else:
        continue
print(sum)


# ⁡⁣⁣⁢6.⁡ ⁡⁣⁣⁢Sum of Squares⁡
# ⁡⁣⁣⁢Question: Given a list [1, 2, 3, 4, 5], print the sum of squares of each number.⁡
# ⁡⁢⁣⁣Hint: Use for loop and num ** 2 → then add all.⁡


squ = [11,12,13,14,15,16,17,18,19,20]

new = []
sum = 0
for i in squ:
    sum = sum + i
    square = i * i
    new.append(square)
print(sum)
print(new)


