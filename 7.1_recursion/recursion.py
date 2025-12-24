
# def sum_is(a,b):
#     c = a + b
#     print(c)

# sum_is(12,13)



# def multi_val(a,b):
#     return a * b

# print(multi_val(12,13))


# def avg_val(a,b,c,d,e):
#     sum = a + b + c + d + e
#     avg = sum / 5
#     return avg 

# print(avg_val(90,9,99,98,89))


# city = ['ahm', 'rajkot','mumbai','kolkata','channai']

# def len_city(a):
#     return len(a) 

# print(len_city(city))


# factorial 

# def fact_num(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact =  fact * i
#     return fact
# print(fact_num(5))



# usa to ind convert 
# def usa_ind(a):
#     return f'the usa is {a} convert in ind is {a * 83}'

# print(usa_ind(3))



# def odd_even(num):
#     if(num % 2 == 0):
#         return 'even'
#     else:
#         return 'odd'
    
# print(odd_even(10))


# ⁡⁢⁣⁢recursion ⁡

# def show(a):
#     if(a == 0):
#         return
#     print(a)
#     show(a - 1)

# show(5)


# factorial
# def fact_num(num):
#     if(num == 0 or num == 1):
#         return 1
#     else:
#         return num * fact_num(num - 1)
    
# print(fact_num(5))


# def sum_natural(n):
#     if(n == 0):
#         return 0
#     return  sum_natural(n - 1) + n

# print(sum_natural(10))

# city = ['ahmedabad','rajkot','veraval','kesod']

# def val_ind(frt,ind=0):
#     if(ind == len(frt)):
#         return
#     print(frt[ind])
#     val_ind(frt,ind + 1)  
# val_ind(city)


# def num_n(n):
#     print('hello python',n)
#     if(n == 5):
#         return
#     else:
#         num_n(n + 1)
    
# num_n(1)



# n = [1,2,4,1,4,3,3,2,30,10]

# total = 14

# for i in range(len(n)):
#     for j in range(i+1):
#         if(n[i] + n[j] == total):
#             print(f'{i},{j} =  {n[i] + n[j]}')


# ⁡⁢⁣⁢factorial⁡
# def fact_num(num):
#     if(num == 0 or num == 1):
#         return 1
#     else:
#         return fact_num(num - 1) * num

# print(fact_num(5))


# ⁡⁢⁣⁢how to work fact ⁡
# def fact5(num):
#     ans = fact4(num -1)
#     fans = ans * num
#     return fans


# def fact4(num):
#     ans = fact3(num -1)
#     fans = ans * num
#     return fans


# def fact3(num):
#     ans = fact2(num -1)
#     fans = ans * num
#     return fans


# def fact2(num):
#     ans = fact1(num -1)
#     fans = ans * num
#     return fans


# def fact1(num):
#     return 1


# print(fact5(5))




# def sum_digit(num):
#     if(num == 0):
#         return 0
#     sans = sum_digit(num // 10)
#     final = sans + num  % 10
#     return final
    

# print(sum_digit(52))




        
# power of n 

# def power_num(num):
#     if(num == 1):
#         return 2
#     else:
#         sans = power_num(num - 1)
#         ans = sans * 2
#         return ans
# print(power_num(5))



# def count_digit(num):
#     if(num > 0 and num < 10):
#         return 1
#     elif(num == 0):
#         return 0
#     sans = num // 10
#     ans = count_digit(sans)
#     return ans + 1

# print(count_digit())



# print n to one 

# def n_to_one(num):
#     if(num == 0):
#         return
#     print(num)
#     n_to_one(num - 1)

# n_to_one(10)



# print one to n 

# def one_to_n(num):
#     if(num == 0):
#         return
#     one_to_n(num - 1)
#     print(num)

# one_to_n(10)



# print one to n table

# def one_to_n(tbl,num):
#     if(num == 0):
#         return
#     one_to_n(tbl,num - 1)
#     print(f'{tbl} x {num} = {tbl * num}')
    
# one_to_n(12,10)


# def factorial(n,fact = 1):
#     if(n <= 0):
#         return fact
#     fact *= n
#     return factorial(n - 1,fact)

# print(factorial(5))


