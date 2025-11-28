

# what is loop ?
# ---> loop is a repete block of code multiple time when condition is setisfy 

# for loop

# syntax

# for variable in sequence:
    #   code to execute


# for i in range(1,4):
#     for j in range(1,3):
#         print(i)

# list = [1,2,3,4,5,6]

# for j in range(len(list)):
#     print(list[j])


# tbl = int(input('Enter number : '))

# for i in range(1,10,1):
#     print(f"{tbl} X {i} = {tbl * i}")


# for i in range(1,20,1):
#     if(i % 2 == 0):
#         print(i,'even number')
#     else:
#         print(i,'odd number')



# for i in range(1,11,1):
#     print('*' * i)

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********


# for j in range(10,0,-1):
#     print('*' * j)

# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *


# ⁡⁣⁣⁢range()⁡ in python is used to generate the sequence of number its most commanly used in loop like a for loop

# syntax 

# ⁡⁢⁣⁣range(start, stop, step)⁡

# start --> (⁡⁢⁢⁣opctional⁡) start  number of the sequence default is ⁡⁣⁣⁢0⁡

# stop --> (⁡⁢⁢⁣required⁡) the sequence stop before this number

# step --> (⁡⁢⁢⁣opctional⁡) the difference between number default ⁡⁣⁣⁢1⁡


# for h in range(1,101,1):
#     print(h)

# # print 1 to 100 number 

# for a in range(4):
#     print(a)

# for b in range(2,7):
#     print(b)

# for g in range(1,10,3):
#     print(g, end= " ")


# for k in range(1,20):
#     if(k > 10):
#         break
#     print(k)

# for l in range(1,10):
#     if(l == 5):
#         continue
#     print(l)


# for r in range(1,15):
#     if(r % 2 == 0):
#         print(r)


# text = 'Python'
# reverse = ''

# for char in text:
#     reverse = char + reverse
# print(reverse)



# txt = 'java'
# rever = '' 
 
# for t in range(len(txt)-1,-1,-1):
#     rever = rever + txt[t]
# print(rever)



# li = ['a','b','c','d']

# st = li.copy()

# for i in range(1,len(li)*2-1,2):
#     st.insert(i,'*')
#     final = ''.join(st)
# print(final)