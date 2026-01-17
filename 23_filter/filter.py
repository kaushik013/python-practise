

# ! filter()

#* Syntax 
#^ var = filter(function,collection) 

#! wap to extract only int from list 

a = [12,3.4,True,'Python',34]

value = filter(lambda n : type(n) == int, a)
print(list(value))


#! extract all value if start with upper case and end with lower case all the touple
 
a = (10,2.3,'Supritha','pythoN','Ugadi')

# print(list(filter(lambda n : type(n) == str and n[0] >= 'A' and n[0] <= 'Z' and n[-1] >= 'a' and n[-1] <= 'z',a)))


#! extract all collection even len

a = [10,2.3,'sakshi',[10,20,30],(7,8),{1,2,3,4}]

print(list(filter(lambda n : type(n) in [str,list,tuple,dict,set ] and len(n) % 2 == 0, a)))

# ! wap to find the square of number from 1 to 20 

new = []
for i in range(1,21):
    new.append(i**2)

print(new)
