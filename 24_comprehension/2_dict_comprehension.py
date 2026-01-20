


#! The phenomenon of creating new dictionary using single line of code is called dictionary comprehension


#^ syntax 

## var= { key: value for var in collection }

## var= { key: value for var in collection  if condition }

## var={key: value1  if condition  else value 2 for var in collection}

# var={key: value for var1,var2 in zip(collection1,collection2)}

## var={key: value for var1,var2 in zip(collection1,collection2) if condition }

#! var= { key: value for var in collection }

result = {i : i ** 2 for i in range(1,6)}
# print(result)


#! From string "Python", create a dictionary where key = character, value = ASCII value


# a = 'Python'

# result = {i : ord(i) for i in a}
# print(result)


#! get following op
##! var= { key: value for var in collection  if condition }

a = 'hello baby are you fine'

result = {i : len(i) for i in a.split() if len(i) % 2 != 0}
# print(result)



# ! get following op 
# {'nayan': 5, 'abcd': 'dcba', 'data': 'atad', 'appa': 4}

##! var={key: value1  if condition  else value 2 for var in collection}


a = ['nayan','abcd','data','appa']

result = {i : len(i) if i == i[::-1] else i[::-1] for i in a}
# print(result)



# get followig op
#! var={key: value for var1,var2 in zip(collection1,collection2)}



a = [1,2,3]
b = [4,5,6]

dic = {}
for i in a:
    for j in b:
        dic[i] = j
# print(dic)


result = {i : j for i,j in zip(a,b)}
# print(result)



##! var={key: value1  if condition  else value 2 for var in collection}
#^op =  {1: 1, 2: 4, 3: 27, 4: 16, 5: 125, 6: 36, 7: 343, 8: 64, 9: 729, 10: 100}


result = {i : i ** 3 if i % 2 != 0 else i ** 2 for i in range(1,11)}
print(result)
