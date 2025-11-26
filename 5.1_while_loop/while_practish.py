

# ⁡⁢⁣⁣seprate the value ⁡
# a = int(input('enter the input : '))


# li = []

# while a >  0:
#     rem = a % 10
#     li.insert(0,rem)
#     a //= 10
# print(li)




# ⁡⁢⁣⁣palindrom or not⁡ 
# rev = 0

# while a > 0:
#     rev *= 10 + a % 10
#     a //= 10
# if(rev == a ):
#     print('palindrom!')
# else:
#     print('not palindrom!')


# ⁡⁢⁣⁣print natural n number⁡
# a = int(input('enter the number : '))

# i = 1
# while  i <= a:
#     print(i)
#     i += 1


# ⁡⁢⁣⁣find natural number⁡ sum
 
# a = int(input('input num : '))

# sum = 0
# i = 1
# while i <= a:
#     sum += i
#     i += 1
# print(sum)



# a = int(input('enter the number : '))

# i = 1
# while i <= 10:
#     print(f'{a} X {i} = {i * a}')
#     i += 1


# ⁡⁢⁣⁢or⁡
# i = 21
# while i <= 30:
#     print(f'{a} X {i-20} = {a * (i-20)}')
#     i += 1


# ⁡⁢⁣⁢factorial⁡
# a = int(input('enter the number : '))

# fact = 1
# i = 1

# while i <= a:
#     fact *= i
#     i += 1
# print(fact)

# ⁡⁢⁣⁣extract vowel from input⁡
# a = input('enter the words : ')

# i = 0 
# vowel = ''
# while i < len(a):
#     if(a[i] in 'AEIOUaeiou'):
#         vowel += a[i]
#     i += 1
# print(vowel)


def define(n):
    digits = []

    while n > 0:
        digit = n % 10
        digits.append(digit)
        n = n // 10
    
    for i in reversed(digits):
        print(i)

define(22)