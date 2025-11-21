

# ⁡⁣⁣⁢7. Numbers Greater Than Average
# Question: Create a list of numbers and print all numbers greater than the average value.⁡
#⁡⁢⁣⁣ Hint: First find average using (sum / len) → then compare each number with it.⁡

num = [12,13,14,15,11,5,34,24,25,6,3]
sum = 0

for i in num:
    sum = sum + i
    avg = sum / len(num)
print(f'total sum is : {sum}')
print(f'sum of avg is : {avg}')

for i in num:
    if(i > avg):
        print(i)
    else:
        continue



# ⁡⁣⁣⁢Find Index of Element
# Question: Write a program to find the index of a given element in a list.⁡
# ⁡⁢⁣⁣Hint: Use list.index(value) method.⁡

ind = [100,200,300,400,500,600,700,800,900,1000]


# ⁡⁣⁢⁣finde all element⁡
for i in range(len(ind)):
    print(f'index is : {i} and element is : {ind[i]}')

print(ind)


# ⁡⁣⁢⁣find which would you w⁡⁣⁢⁣ant⁡
find = int(input('enter element would you access : '))
if(find in ind):
    index = ind.index(find)
    print(f'index is {index} and element is {find}')
else:
    print('not found!')




# ⁡⁣⁣⁢Merge Two Sorted Lists
# Question: Merge two sorted lists into a single sorted list.⁡
# ⁡⁢⁣⁣Hint: Use + to join both lists → then use sorted().⁡


list1 = [1,5,6,3,5,3]
list2 = [5,3,2,4,5,7,5]

list3 = list1 + list2
print(list3)

list3.sort()
print(list3)
# [1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 6, 7]



# ⁡⁣⁣⁢🧩 10. Find Repeated Numbers
# Question: Find all numbers that appear more than once in a list.⁡
# ⁡⁢⁣⁣Hint: Use a loop with count() method → print if count(num) > 1.⁡

mark = [22,22,22,33,44,44,55,55,45]

for i in mark:
    mark.count(i)
    if(mark.count(i) > 1):
        print(i)
    else:
        continue