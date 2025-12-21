

# 1.Input : (12,3.4,'hello',2+3j,'python','bye',False)

#  Output : {'hello': 5, 'python': 6,'bye':3} 

# 2.Input : [12,3.4,'hello',2+3j,'python','bye',False]
#  Output : {'hello': 'ho', 'python': 'pn','bye':'be'}

# 3.Input : 'aPpLe#123'
#  Output : {'a':'A', 'P':'p', 'p':'P',  'L':'l', 'e':'E'}

# 4.Input=['apple','banana','orange','kiwii']
# output= {'apple':5,'banana':'ananab','orange':'egnaro','kiwii':5}


# 6.Input={'star':10,'byee':30,'moon':80}
#   Output={10:'star',30:'byee',80:'moon'}


# 7.Write a program to get the following output

# s='example on for loop'
# out='ee on fr lp'


# 8.Write a program to get the following output
# s='abcabccabbb'
# out={'a':3,'b':5,'c':3}


# 9.Input='abcabacbcc'
#   output='a3b3c4'


# 10.l=['p1.py','file2.txt','file1.py','google.com','data.txt']
#    output={'py':['p1','file1'],'txt':['file2','data'],'com':['google']}


# 11.Write a program to print all the divisors of a given number

# 12.Write a program to check whether the given number is perfect number or not

# 13.Write a program to check whether the given number is Armstrong number or not








# //! ans

#//* 1.
# input  = (12,3.4,'hello',2+3j,'python','bye',False)
# {'hello': 5, 'python': 6, 'bye': 3}

# a = (12,3.4,'hello',2+3j,'python','bye',False)

# dic = {}

# for i in a:
#     if(type(i) == str):
#         dic[i] = len(i)
# print(dic)



# 2.Input : [12,3.4,'hello',2+3j,'python','bye',False]
#  Output : {'hello': 'ho', 'python': 'pn','bye':'be'}

# a =  [12,3.4,'hello',2+3j,'python','bye',False]

# dic = {}

# for i in a:
#     if(type(i) == str):
#         dic[i] = i[0]+i[-1]
    
# print(dic)




# 3.Input : 'aPpLe#123'
#  Output : {'a':'A', 'P':'p', 'p':'P',  'L':'l', 'e':'E'}

# a = 'aPpLe#123'

# dic = {}

# for i in a:
#     if(type(i) == str):
#         upper = chr(ord(i) - 32)
#         lower = chr(ord(i) + 32) 
#         if(i >= 'A' and i <= 'Z'):
#             dic[i] = lower
#         elif(i >= 'a' and i <= 'z'):
#             dic[i] = upper
        
# print(dic)




# 4.Input=['apple','banana','orange','kiwii']
# output= {'apple':5,'banana':'ananab','orange':'egnaro','kiwii':5}


# a  = ['apple','banana','orange','kiwii']

# dic = {}

# for i in a:
#     if(len(i) % 2 == 0):
#         dic[i] = i[::-1]
#     else:
#         dic[i] = len(i)
# print(dic)




# 6.Input={'star':10,'byee':30,'moon':80}
#   Output={10:'star',30:'byee',80:'moon'}

# a = {'star':10,'byee':30,'moon':80}

# dic = {}

# for i in a:
#     dic[a[i]] = i

# print(dic)



# 7.Write a program to get the following output

# s='example on for loop'
# out='ee on fr lp'

# a = 'example on for loop'


# new = ''

# for i in a.split():
#     new += i[0]+i[-1] + ' '

# print(new)




# 8.Write a program to get the following output
# s='abcabccabbb'
# out={'a':3,'b':5,'c':3}

# a = 'abcabccabbb'

# dic = {}

# for i in a:
#     if(i not in dic):
#         dic[i] = 1
#     else:
#         dic[i] += 1

# print(dic)





# 9.Input='abcabacbcc'
#   output='a3b3c4'


# a = 'abcabacbcc'

# result = ""

# for i in a:
#     if i not in result:
#         count = a.count(i)
#         result += i + str(count)
# print(result)

    

# 10.l=['p1.py','file2.txt','file1.py','google.com','data.txt']
#    output={'py':['p1','file1'],'txt':['file2','data'],'com':['google']}


a = ['p1.py','file2.txt','file1.py','google.com','data.txt']

dic = {}

for i in a:
    new = i.split('.')
    key = new[-1]
    value = new[0]
    if(key not in dic):
        dic[key] = [value]
    else:
        dic[key] = dic[key] + [value]

print(dic)

    

# 11.Write a program to print all the divisors of a given number


# new = []

# a = int(input('enter the num : '))

# for i in range(1,a+1):
#     if(a % i == 0):
#         new.append(i)

# print(new)




# 12.Write a program to check whether the given number is perfect number or not

# a = int(input('enter the num : '))

# total = 0

# for i in range(1,a):
#     if(a % i == 0):
#         total += i
    
# if(total == a):
#     print(f'{a} is perfect number!')
# else:
#     print(f'{a} is not perfect number!')




# 13.Write a program to check whether the given number is Armstrong number or not

# a = input('enter the num : ')

# temp = int(a)

# total = 0

# for i in a:
#     total += int(i) ** 3

# if(total == temp):
#     print('arm strong number!')
# else:
#     print('not arm strong number!')


