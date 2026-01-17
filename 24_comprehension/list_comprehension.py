
#  list comprehension

# syntax :

#! 1 var = [val for var in collection]

#! 2 var = [val for var in collection if condition]

#! 3 var = [T.S.B if condition else F.S.B. for var in collection]

#! 4 = var = [val1,val2 for var1 in collection 1 for var2 in collection 2]


# find the square of number between 1 to 20

# new = []
# for i in range(1,21):
#     new.append(i ** 2)
# print(new)


#* using list comprehension
#! 1 var = [val for var in collection]


square = [i ** 2 for i in range(1,21)]
print(square)


#& type 2 

#! program to create a list consists of squares of each and every integer between 1 to 20 only if it is multiple of 3  

#! 2 var = [val for var in collection if condition]

var = [i ** 2 for i  in range(1,21) if i % 3 == 0]
print(var)


# type 3
#  program to store the squares of integers if integer is even keep square else store cube of the integer from the 1 to 20



#! 3 var = [T.S.B if condition else F.S.B. for var in collection]


var = [i**2 if i % 2 == 0 else i ** 3  for i in range(1,21) ]
print(var)
