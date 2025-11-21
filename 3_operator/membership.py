

# ⁡⁢⁣⁣member ship operator⁡

# membership operator are used to check if value is present or not in sequence -->(👉 string, list, tuple,
#  or dictionary.)

# ---> return Boolean value True or False

#⁡⁣⁣⁢ 1. in (present) ⁡
# --> Returns True if the value exists in the sequence


film = ['yoodha', 'malang', 'polo', 'durty monry']

print('malang' in film) # True
print('yug' in film) # False



# 2. ⁡⁣⁣⁢not in (not prasent)⁡
# --> check if element not exist in sequence return true

fruits = ('graps', 'apple', 'mango')

print('mango' not in fruits) # False
print('banana' not in fruits) # True




# example 

name = input("Enter your name : ")

if name in ['kajal','radha','riddhi','neha','janvi']:
    print(name, 'you are welcome !')
else:
    print(name,'not found !')


