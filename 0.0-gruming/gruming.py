
#//! lambda 

# lambda is a anonumos function because it has no name 

# a = lambda n: 'even' if(n%2 == 0) else'odd'

# print(a(10))



# a = lambda n: n%2 == 0
# print(a(10))



# func = lambda n: n **2

# a = map(func,range(1,21))
# print(list(a))


#//! only one line map + lambda
# print(list(map(lambda n: n**2,range(1,21))))

# a = 'hi hello how are you'

# new = a.split()

# a = map(lambda f: f[0]+f[-1],new)
# print(list(a))


#//! extract the int 
# a = [12,13,14,'hii','hrllo',True]

# fun = lambda n: type(n) == int

# # b = filter(fun, a)
# print(list(b))

# print(list(filter(fun,a)))


# t = (10,2.3,'Supritha','home','pythoN','Ugadi')

# print(list(filter(lambda i: type(i) == str and (i[0]>= 'A' and i[0] <= 'Z') and (i[-1] >= 'a' and i[-1] <= 'z'),t)))


# name = ['kaushik','raj','mayur','dharmesh']

# mark = [90,65,76,87]

# d = {i:j for i,j in zip(name,mark) if j> 50}
# print(d)
  


# result = [i*i for i in range(1,6)]

# print(result)


# result = list(i+i for i in range(1,6))

# print(result)

# names = ['kaushik','janvi','jay','kajal']


# result = list(i for i in names if i.startswith('k'))
# print(result)


# a = 'good morning ahmedabad'

# result = {i : ('even' if i%2 == 0 else 'odd') for i in range(1,11)}
# print(result)

# result = {i : (i*i if i % 2 == 0 else  i**3) for i in range(1,10) }
# print(result)


# result = lambda i : i+i

# print(result(12))

