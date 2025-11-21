
# ⁡⁢⁣⁣what is while loop?⁡
# ---> while loop is keep running as long as a condition is True

# ⁡⁣⁣⁢syntax⁡
# while condition:
    # code to execute


# ⁡⁣⁣⁢chech statment⁡
age = 18
while age >= 18:
    print('can vote')
    break


# ⁡⁣⁣⁢count str⁡
text = 'pyrhon develop'
i = 0

while i < len(text):
    i = i + 1
print(i)


i = 0 
while i < 4:
    i = i + 1
    print(i)
else:
    print('not printed')

# ⁡⁣⁣⁢print all loop⁡

# ⁡⁣⁣⁢can not print loop⁡
i = 0 
while i < 4:
    i = i + 1
    print(i)
else:
    print('not printed')


a = 0
b = 'geeks for geeks'

while a < len(b):
    a = a + 1
    print(a)
    pass
print('value of a is,',a)


a = 0
b = 'geeks for geeks'

while a < len(b):
    if(b[a] == 'e' or b[a] == 's'):
        a = a + 1
        break
    print(b[a])
    a = a + 1
    print(a)



