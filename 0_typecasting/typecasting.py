
# type casting


# ⁡⁢⁣⁣int into other ⁡
print('int into other...')
a = 100
print(int(a))
# 100

print(float(a))
# 100.0

print(bool(a))
# True

print(complex(a))
# (100+0j)

print(str(a))
# '100'


# ⁡⁢⁣⁣float into another⁡

print('float into another...')

b = 100.10
print(int(b))
# 100

print(float(b))
# 100.10

print(bool(b))
# True

print(complex(b))
# (100.10+0j)

print(str(b))
# '100'


# ⁡⁢⁣⁡⁢⁣⁣complex into another⁡
print('complex into another')

b = (8+9j)

# print(int(b))
# error

# print(float(b))
# error

print(complex(b))
# (8+9j)

print(bool(b))
# true

print(str(b))
'(8+9j)'


# ⁡⁢⁣⁣bool into another⁡
print('bool into another')

k = True
j = False

print(int(k)) # 1
print(int(j)) # 0

print(float(k)) # 1.0
print(float(j)) # 0.0

print(bool(k)) # true
print(bool(j)) # false

print(complex(k)) # (1+0j)
print(complex(j)) # 0j

print(str(k)) # true
print(str(j)) # false

h = '123'
print(int(h))



# ⁡⁢⁣⁣string into another⁡
print('string into another')

l = 'hello'

print(bool(l)) # True

print(list(l)) # ['h', 'e', 'l', 'l', 'o']

print(tuple(l)) # ('h', 'e', 'l', 'l', 'o')

print(set(l)) # {'e', 'l', 'h', 'o'}
