

# ⁡⁢⁣⁣for loop in python ⁡


# for i in range(1,21,1):
#     print(i)

# for i in range(20,0,-1):
#     print(i)


# a = int(input('enter number : '))

# for i in range(1,11,1):
#     print(f'{a} X {i} = {a*i}')

# a = 'Kaushik'

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)


# ⁡⁢⁣⁣break statment⁡
# name = 'Chariya kaushik'

# for i in name:
#     if(i == 'k'):
#         break
#     print(i)

# ⁡⁢⁣⁣continue statment⁡
# for i in range(1,10,1):
#     if(i == 5):
#         continue
#     print(i)



# for i in range(1,10,1):
#     if(i == 12):
#         print('break statment is  execute!')
#         break
#     print(i)
# else:
#     print('break statment is not executed!')


# ⁡⁢⁣⁣natural number⁡
# n = int(input('enter number : '))

# for i in range(n+1):
#     print(i)


# ⁡⁢⁣⁣reverse natural number⁡
# n = int(input('enter natural num : '))

# for i in range(n,0,-1):
#     print(i)


# ⁡⁢⁣⁣table⁡

# n = int(input('enter number : '))

# for i in range(1,11,1):
#     print(f'{n} X {i} = {i*n}')


# ⁡⁢⁣⁣natural sum of n ⁡
# n = int(input('enter number : '))

# sum = 0
# for i in range(1,n+1):
#     print(i)
#     sum += i
# print('total : ', sum)


#⁡⁢⁣⁣ factorial⁡
# n = int(input('enter number : '))
# fact = 1
# for i in range(1,n+1,1):
#     fact *= i
# print(fact)


# ⁡⁢⁣⁣sum of 10 number⁡

# sum = 0

# for i in range(1,11,1):
#     sum += i
# print(sum)


# fact = 1
# n = int(input('enter number : '))
# for i in range(1,n+1,1):
#     fact *= i
# print(fact)



# ⁡⁢⁣⁣print sum of even or odd ⁡
# even = 0
# odd = 0

# for i in range(1,21,1):
#     if(i%2 == 0):
#         even += i
#     else:
#         odd += i
# print(even)
# print(odd)




# ⁡⁢⁣⁣all factor number :⁡

# n = int(input('enter the number : '))

# for i in range(1,n+1):
#     if(n%i == 0):      
#         print(f'factor is {i}')
# print(f'all factor of = {n}')


# ⁡⁢⁣⁣perfect number or not ⁡

# n = int(input('enter the number : '))
# sum = 0
# for i in range(1,n):
#     if(n%i == 0):
#         sum += i

# if(sum == n):
#     print(f'{n} is perfect number!')
# else:
#     print(f'{n} is not perfect number!')


# ⁡⁢⁣⁣number is prime or not ⁡

# n = int(input('enter the number : '))
# count = 0
# for i in range(1,n+1):
#     if(n%i == 0):
#         count += 1

# if(count == 2):
#     print('prime number!')
# else:
#     print('not prime number!')


# n number of prime numbers

# a = int(input('enter the number: '))
# prime = []
# for i in range(1, a+1):
#     count = 0
#     for j in range(1,i+1):
#         if(i%j == 0):
#             count += 1
#     if(count == 2):
#         prime.append(i)
# print(prime)





# a = 'this is easy'
# #output = 'ysae si siht'

# li = a.split()
# new = ''

# for i in range(len(li)-1,-1,-1):
#     new = new + ' ' + li[i][::-1]
# print(new)




# b = 'this is easy'
#output =  siht si ysae

# li1 = b.split()
# new1 = ''
# for i in range(0,len(li1)):
#     new1 = new1 + ' ' + li1[i][::-1]

# print(new1)





# a = 'this is easy'

# new = ''

# for i in range(len(a)-1,-1,-1):
#     new += a[i]
# print(new)





#1.from string "python" ,create a dictionary where key = character,value=ascii value
# {'P': 80, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}

# a = 'Python'

# dic = {}

# for i in a:
#     dic[i] = ord(i)
# print(dic)





# given nums = [10,-5,8,-3,0,12],create a dictionary with key = number,value="positive" only for 
# positive numbers.

# a = [10,-5,8,-3,0,12]

# dic = {}

# for i in a:
#     if(i >= 0):
#         dic[i] = 'positive'

# print(dic)



# a = ['Apple','Banana','Cherry','Dates','Orange','Ice apple']
# #output = {'Apple': 'A', 'Banana': 'b', 'Cherry': 'c', 'Dates': 'd', 'Orange': 'O', 'Ice apple': 'I'}

# dic = {}

# for i in a:
#     if(i[0] in 'AEIOUaeiou'):
#         dic[i] = i[0]
#     else:
#         dic[i] = chr(ord(i[0])+ 32)

# print(dic)




# #4.get the following output
# #find average marks,then creat a dictionary {name:"Above Avg" or "below Avg"}

# a = ['Ananya','Rohit','Sneha','Aarav','Meena']

# b = [85,72,90,67,88]

# total  = 0

# uppp = {}


# for i in b:
#     total += i
# avg = total / len(b)

# for i in range(len(a)):
#     if(b[i] > avg):
#         uppp[a[i]] = 'above avg'
#     else:
#         uppp[a[i]] = 'below avg'
# print(uppp)



#5.from the string "programming",count occurances of each character using dictionary comphrehension.
# a = 'programming'


# dic = {}

# for i in a:
#     if(i not in dic):
#         dic[i] = 1
#     else:
#         dic[i] = dic[i] + 1
# print(dic)




#6.get the following output
# # s="python is fun and python is easy"
# # output={'python':2,'is':2,'fun':1,'and':1,'easy':1}

# s = 'Python is fun and Python is easy'

# dic = {}

# for i in s.split():
#     if(i not in dic):
#         dic[i] = 1
#     else:
#         dic[i] = dic[i]+1

# print(dic)



#  1.program to extract string from the list only if it is palindrome

# l = ['hi',100,3.2,'madam','appa','bye']

# pallindrom = []

# for i in l:
#     if (type(i) == str):
#         if(i == i[::-1]):
#             pallindrom.append(i)

# print(pallindrom)




# a = "python is fun and python is easy"
# # output={'python':2,'is':2,'fun':1,'and':1,'easy':1}

# s = 'programs based open comprehension happy'

# new = s.split()


# li = []

# for i in new:
#     if(len(i) % 2 == 0):
#         li.append(i)
#     else:
#         li.append(i[0]+i[-1])

# print(li)


# n = [[1,2],[3,4],[5,6]]

# li = []

# for i in n:
#     for j in i:
#         li.append(j)

# print(li)


# #5.convert temperature in to fahrenheit
# temp=[0,20,37,100]
# convert to each to fahrenheit using formula
# f=(c*9/5)+32

# temp = [0,20,37,100]

# temprac = []

# for i in temp:
#     f = (i * 9/5) + 32
#     temprac.append(f)

# print(temprac)




# a = ['virat','rohit','rahul','kaushik']

# b = [10,20,30,40]

# c = ['s1001','s1002','s1003','s1004']

# out = [{{s1001} : {virat : 10}, {s1002} : {rohit : 20}, {s1003} : {rahul : 30}, {s1004} : {kaushik : 40}}]

# final = [{}]


# for i in range(len(a)):
#     final.append()


# print(final)

