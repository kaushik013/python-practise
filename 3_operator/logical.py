

# logical oprerator

# ----> logical operator are used to combine two or more condition 
# they return True or False depending where condition is setisfy


# ⁡⁢⁣⁣⁡⁢⁣⁣Types of Logical Operators⁡

# 1. and
# 2. or
# 3. not



# ⁡⁣⁣⁢1. and (logical and)⁡
# ---> it means both condition is True

a = 10
b = 5
print(a > b and b < a ) # True
# ✅ Both are true → Result is True

# example

print([] and set())
# []

print(3.4 and 22)
# 22

print(False and True)
# false

print(True and False)
# false


# ⁡⁣⁣⁢2. or(logical or)⁡
# ---> return True if any one condition is True)

c = 10
d = 2
print(c > d or d > c) # True
# ✅ One condition is true → Result is True

print(c >= 10 or c%2==0)



# ⁡⁣⁣⁢3. not(logical not)⁡
f = 90
g = 45
print(not(f > g)) # False



# example
a = 300
b = 2040

if(a > b and b < a):
    print(a,' a is gratest numbet')
else:
    print(b,' b is gratest number')



# ⁡⁢⁣⁢example⁡

print(not True)
# false

print(not False)
# true

print(not 'kaushik')
# false

print(not 0)
# true

print(not [])
# true

print(not [1,2])
# false

print(not 6+7j)
# false

