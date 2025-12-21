
# //! zip function()

# a = [72,83,94,55,76]
# b = ['kaushik','janvi','raj','gita','ram']


# for i,j in zip(a,b):
#     print(i,j)


# //! enumerate function()

# a = [12,13,14,15,16,17]

# for i,j in enumerate(a):
#     print(i,j)


#//! user define function 

# syntax : 


# def fname(args):     # function declaraction
#     s.b

# fname()       # function call


# //^ type of function

# //* function without args and without return
# //* function with args and without return
# //* function without args and with return
# //* function with args and with return



# extract wowel in string

# //! without
# a = 'hello world'

# vowel = ''

# for i in a:
#     if(i in 'AEIOUaeiou'):
#         vowel += i
# print(vowel)


# //* function without args and without return
# //! function
# def vowel_string():
#     a = input('enter name : ')

#     new = ''
#     for i in a:
#         if(i in 'AEIOUaeiou'):
#             new += i
#     print(new)

# vowel_string()


# //* function with args and without return

# even or odd 

# def even_odd(a):
#     if(a % 2 == 0):
#         print(f'{a} is even!')
#     else:
#         print(f'{a} is odd!')

# even_odd(12)


# given list is homogenous or hetrogenous

# def check_list(a):
#     check = type(a[0])
#     for i in a:
#         if(type(i) != check):
#             print('hetrogenous!')
#             break
#     else:
#         print('homogenous!')

# b = eval(input('enter list : '))       
# check_list(b)



# //* function without args and with return

# def check_str():
#     a = eval(input('enter the list : '))
#     new = []
#     for i in a:
#         if(type(i) == str):
#             new.append(i)
#     return new


# print(check_str())


# a = ['Rs1500','3000','30,000','1,500','1200$']

# a = [1500,3000,30000,1500,1200]
  

# check perfect or not
# def check_per(n):
#     sum = 0
#     for i in range(1,n):
#         if n % i == 0:
#             sum += i
#     if(sum == n):
#         return 'perfect'
#     else:
#         return 'not perfect!'

# print(check_per(69))



#//! pakking and aun packing


#//* tuple single pakking

# def demo(*args):
#     return args

# print(demo(12,13))
# print(demo())


#//! Example
# def sum_num(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(sum_num(12,13,14,15))


#//! dictionary / double pakking

def key_val(**kwargs):
    return type(kwargs),kwargs

# print(key_val(a = 10, b = 20, c = 30 ))



def all_off(*args, **kwargs):
    print(args)
    print(kwargs)

# all_off(12,13,14,a='hii',b = 'hello')



# unpakking  

a = [12,13,14]

def unpakking(a,b,c):
    print(a)
    print(b)
    print(c)

# unpakking(*a)


def unpaking(a,b,c):
    print(a)
    print(b)
    print(c)

d = 'JAY'
# unpaking(*d)

# unpaking(*{'jay':10,'kaushik' : 12, 'janvi' :13})






