
# with open('text','w') as wrt:
#     wrt.write('hello i am kaushik')

# with open('text','r') as wrt:
#     result = wrt.read()
#     ttl = 0
#     for i in result:
#         if(i == ' '):
#             continue
#         else:
#             ttl += 1
#     print(ttl)


#^ extract the ttl wrold
# with open('text','r') as wrt:
#     result = wrt.read()
#     data = result.split()
#     print(len(data))


#! write a profram to find no of time a perticular char is repeted in the text data

# data = 0

# a = input('entee the txt : ')

# with open('text','r') as wrt:
#     result = wrt.read()
#     print(result.count(a))



#! num of line prasent in file 


# with open('text','r') as wrt:
#     result = wrt.readlines()
#     print(len(result))



#! write dic or word is ey and repeat is count 

# dic = {}

# with open('text','r') as wrt:
#     result = wrt.read()
#     for i in result:
#         if(i == ' '):
#             continue
#         elif i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] += 1

# print(dic)


# dic = {}
# with open('text','r') as wrt:
#     result = wrt.read()
#     new = result.split()
#     for i in new:
#         if i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] += 1

# print(dic)

