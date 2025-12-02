
# 1.Write a program to extract all the lower case character from the given string only if its ascii value 
# is even 

# 2..Write a program to find the length of the longest word  from the string

# 3. Write a program to display all the numbers which are divisible by 13 but not by 
# between 100 and 500.




# 1.Write a program to extract all the lower case character from the given 

# a = input('enter the string  : ')

# temp = ''

# for i in range(len(a)):
#     if(a[i] >= 'a' and a[i] <= 'z'):
#         if(ord(a[i]) % 2 == 0):
#             temp += a[i]
# print(temp)




# 2..Write a program to find the length of the longest word  from the string

# a = input('enter the sreing : ')


# words = a.split()

# empt = ''
# final = 0

# for i in range(0,len(words)):
#     if(len(words[i]) >= final):
#         final = len(words[i])
#         empt = words[i]

# print(f'the longest word length is : "{final}" and word is "{empt}" ')


# 3. Write a program to display all the numbers which are divisible by 13 but not by 
# between 100 and 500.


# for i in range(1,1000):
#     if(i % 13 == 0):
#         if(i >= 100 and i <= 500):
#             continue
#         else:
#             print(i)



# reverse the string 

# a = input('enter the text : ')

# reverse = ''

# for i in range(len(a)-1,-1,-1):
#     reverse += a[i]
# print(reverse)



# extract wovel
# a = input('enter the text : ')

# extWovl = ''

# for i in a:
#     if(i in 'AEIOUaeiou'):
#         extWovl += i
# print(extWovl)
