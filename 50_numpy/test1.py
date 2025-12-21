# 1.Write a program to remove duplicates from the list

# 2.To get the following output

# s='abcaabcbbb'
# out={'a':3,'b':5,'c':2}

# 3.Write a program to print prime numbers upto n

# 4.  1
#     1 2
#     2 3 4
#     4 5 6 7
#     7 8 9 10 11
    

# Write a program to print above pattern

# 5.Write any 4 inbuilt functions in string along with appropriate examples

# 6.Print numbers between 1 to 50 by skipping 3 and 15

# 7.l1=['Python','Java','C++']
   
#    l2=[345,78,56]

#    output={'Python':345,'Java':78,'C++':56}



#//! 1.Write a program to remove duplicates from the list

# a = [12,13,12,131,4,141,14,12,13,14,15]


# new = []
# for i in a:
#     if(i not in new):
#         new.append(i)
# print(new)



#//! 2.To get the following output

# s='abcaabcbbb'
# out={'a':3,'b':5,'c':2}


# a = 'abcaabcbbb'

# dic = {}

# for i in a:
#     if(i not in dic):
#         dic[i] = 1
#     else:
#         dic[i]+= 1
# print(dic)



# 3.Write a program to print prime numbers upto n

# a = int(input('enter the num : '))

# prime = []

# for i in range(2,a+1):
#     for j in range(2,i):
#         if(i % j == 0):
#             break
#     else:
#         prime.append(i)
# print(prime)

        



 
#//! 4.Write a program to print above pattern
#     1
#     1 2
#     2 3 4
#     4 5 6 7
#     7 8 9 10 11
    


# start = 1

# for i in range(1, 6):
#     num = start
#     for j in range(i):
#         print(num, end=' ')
#         num += 1
#     print()
#     start = num - 1



# 5.Write any 4 inbuilt functions in string along with appropriate examples

#//* string :- it is a collection of a multiple character

#//^ 1. upper()

# a = 'kaushuk'
# b = a.upper()
# print(b)


# //^ 2. lower()
# c = 'THIS IS a Qspider'
# d = c.lower()
# print(d)


# //^ 3. replace()
# name = 'Python'
# new = name.replace('t','k')
# print(new)


# //^ 4. capitalize

# city = 'ahmedabad'
# new_city = city.capitalize()
# print(new_city)



#//! 6.Print numbers between 1 to 50 by skipping 3 and 15

# for i in range(1,51):
#     if(i == 3 or i == 15):
#         continue
#     print(i)


#//! 7.
# l1=['Python','Java','C++']
# l2=[345,78,56]

#    output={'Python':345,'Java':78,'C++':56}

# a = ['Python','Java','C++']
# b = [345,78,56]

# dic = {}

# for i,j in zip(a,b):
#     dic[i]=j

# print(dic)





# a = ['RS2000','3000','1,500','7500']

# new = []

# for i in a:
#     accept = ''
#     for j in i:
#         if(j >= 'A' and j <= 'Z' or j >= 'a' and j <= 'z'):
#             continue
#         elif (j>= '0' and j <= '9'):
#             accept += j
#         else:
#             continue
            
#     new.append(int(accept))
# print(new)


# a = [5,6,2,3,4,3,2]
# b = [10,20,30,40,30,20,10]

# new = []

# for i,j in zip(a,b):
#     new.append(i*j)
# print(new)






