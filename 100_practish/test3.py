

#//! factorial

# a = int(input('enter the num :'))

# fact = 1

# for i in range(1,a+1):
#     fact *= i
# print(fact)



#//! ascii values of all UPPER case

# for i in range(65,91,1):
#     print(chr(i),i)


# li = []

# for  cube = i ** 3
#     li.append(cube)
    
# print(li)



#//! sum of int in hetrogenous
# a = [12,'yes',13,12.34,12,True,False,'hii','hello']

# sum = 0

# for i in a:
#     if(type(i) == int):
#         sum += i
# print(sum)



# extract all the integer from the list which are multiple of  5 and is three digit number

# a = [122,150,100,342,242,3,3535,353,645,3,32,442]

# for i in a:
#     if(i % 5 == 0 and i >= 100 and i <= 999):
#         print(i)



# ! balance num 

# a = int(input('enter the num : '))

# new = str(a)
# check = len(str(a))
# mv = len(new) // 2

# if(check % 2 != 0):
#     left = 0
#     for i in range(0,mv):
#         left += int(new[i])
#     right = 0
#     for j in range(mv+1,len(new)):
#         right += int(new[j])
#     if(right == left):
#         print('balance num')
#     else:
#         print('not balance num')
# else:
#     left = 0
#     for i in range(0,mv-1):
#         left += int(new[i])
#     right = 0
#     for j in range(mv+1,len(new)):
#         right += int(new[j])

#     if(right == left):
#         print('balance num')
#     else:
#         print('not balance num')



# a = int(input('enter the num : '))

# new = str(a)
# mv = len(new) // 2

# left = 0
# for i in range(0,mv-1):
#     left += int(new[i])

# right = 0
# for j in range(mv+1,len(new)):
#     right += int(new[j])

# if(right == left):
#     print('balance')
# else:
#     print('not')


# d = {}

# for i in [1,2,3,4,5,6,7,8,9]:
#     if (i % 3 not in d):
#         d[i % 3] = [i]
#     else:
#         d[i%3].append(i)
# print(d)



# 1
# 1 2
# 2 3 4
# 4 5 6 7
# 7 8 9 10 11

# start = 1

# for i in range(1, 6):
#     for j in range(i):
#         print(start, end=' ')
#         start += 1
#     print()
#     start -= 1


# n = 5
# a = 1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(a,end=' ')
#         a += 1
#     a -= 1
#     print()


# 1 
# 1 2 
# 2 3 4 
# 4 5 6 7 
# 7 8 9 10 11 

