
#! map()

# var = map(func,collection)

# ! collection should be homogenous
# ! no of input collection == no of op collection


#* find the square of each and every value from the below list 

# a = [12,13,14,15,16]
# collection = lambda n : n ** 2

# sqr = map(collection,a)
# print(list(sqr))

#^ or

# a = [12,13,14,15,16]

# final = map(lambda n : n ** 2,a)
# print(list(final))


#! wap to get the following op 
# op = ['python','java','holiday','people']

# row = lambda n : n[0]+n[-1]

# result = map(row,op)
# print(list(result))

#^ or 

# op = ['python','java','holiday','people']
# final = map(lambda n : n[0]+n[-1],op)
# print(list(final))


#^ or 

# print(list(map(lambda n : n[0]+n[-1],['python','java','holiday','people'])))



#! a = ['abcd','start','data','python']

# row = lambda n: len(n)
# final = map(row,a)
# print(list(final))


#^ or 

# print(list(map(lambda n : len(n),['abcd','start','data','python'])))


# write the p to get the dfollowing oop
# ! {1:1,2:4,3:9.....10:100}

# a = list(range(1,11))

# result = dict(map(lambda n : (n , n**2 ),list(range(1,11))))
# print(result)


#! get following op 
# a = ['python','java','holiday','people']

# result = dict(map(lambda n : (n , len(n)), a))
# print(result)

#^ or

# print(dict(map(lambda n : (n, len(n)), ['python','java','holiday','people'])))