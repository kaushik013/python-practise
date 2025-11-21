

# ⁡⁣⁣⁢print nagative number different and positive different ⁡

num = [-12,33,12,-11,-29,39,43,-43,54]

print('positive number')
for i in num:
    if(i >= 0):
        print(i)

print('nagative number')
for i in num:
    if(i < 0):
        print(i)


#⁡⁣⁣⁢ print the avg of sum⁡

mark = [67,87,98,78,67,98,99]
sum = 0
for i in mark:
    sum += i
print(f'total sum is {sum}')
print(f'total avg is :{sum / len(mark):.2f}%')


# ⁡⁣⁣⁢define largest number⁡

collection = [12,23,65,76,455,67,6,54]

large = collection[0]
index = 0

for i in range(len(collection)):
    if(collection[i] > large):
        large = collection[i]
        index  = i
print(f'largest number is a {large} and index is a {index}')





# ⁡⁢⁣⁡⁣⁣⁢define largest and second largest number

number = [12,3,2,53,655,76,878,56,45,32,775]

largest = number[0]
l_index = 0
sec_largest = number[0]
s_index = 0

for i in range(len(number)):
    if number[i] > largest:
        sec_largest = largest
        s_index = l_index
        largest = number[i]
        l_index = i
    elif(number[i] > sec_largest):
        sec_largest = number[i]
        s_index = i


print(f'largest number is {largest} and index is {l_index}')
print(f'sec_largest number is {sec_largest} and index is {s_index}')

