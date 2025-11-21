


# ⁡⁢⁣⁣elif statment⁡


# check digit one or two or three or more than 3 digit⁡
# n = int(input('enter the num : '))

# if(n >= 1 and n<= 9):
#     print('single digit!')
# elif(n >=10 and n<= 99):
#     print('double digit!')
# elif(n >=100 and n<= 999):
#     print('three digit!')
# else:
#     print('more than 3digit')


# # ⁡⁢⁣⁣both are same!⁡
# if( 0<=n<=9):
#     print('single digit!')
# elif(10<=n<=99):
#     print('double digit!')
# elif(100<=n<=999):
#     print('three digit!')
# else:
#     print('more than 3digit')


# n = input('enter the character! : ')

# ⁡⁢⁣⁣first way⁡
# if(n in '1234567890'):
#     print('digit!')
# elif(n == n.upper()):
#     print('upper case char!')
# elif(n == n.lower()):
#     print('lower char!')
# else:
#     print('special char!')


# ⁡⁢⁣⁣second way⁡
# if('0'<=n<='9'):
#     print('digit!')
# elif('A'<=n<='Z'):
#     print('upper case char!')
# elif('a'<=n<='z'):
#     print('lower char!')
# else:
#     print('special char!')



# ⁡⁢⁣⁣check which number is gratest⁡
# a = int(input('enter first number : '))
# b = int(input('enter second number : '))
# c = int(input('enter third number : '))

# if(a == b == c):
#     print('all number equal!')
# elif(a == b):
#     print('a and b is similar!')
# elif(a == c):
#     print('a and c is similar!')
# elif(b == c):
#     print('b and c is similae!')
# else:
#     if(a > b and a > c):
#         print(f'{a} is gratest!')
#     elif(b > a and b > c):
#         print(f'{b} is gratest!')
#     else:
#         print(f'{c} is gratest!')


# a = int(input('enter the number  : '))

# if(a%3 == 0 and a%5 == 0):
#     print('fizz-buzz!')
# elif(a%3):
#     print('fizz!')
# elif(a%5):
#     print('buss!')
# else:
#     print('not divisable by 3 and 5')


# l = ["java","python"]
# s = ""
# for i in l:
#     for j in i:
#         s+=j

# print(s[0:4])
# print(s[4:11])



# ⁡⁢⁣⁣given year is leap year or not ⁡

# year = int(input('enter the year : '))

# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f'{year} is leap year!')
# else:
#     print(f'{year} not leap year!')


# ⁡⁢⁣⁣give number smallest ⁡

a = int(input('enter the first number : '))
b = int(input('enter the second number : '))
c = int(input('enter the third number : '))



if(a == b == c):
    print('all number are similar!')
elif(a == b):
    print('a and b is similar!')
elif(a == c):
    print('a and c is similar!')
elif(b == c):
    print('b and c is similar!')
else:
    if(a < b and a < c):
        print(f'{a} is smallest!')
    elif(b < a and b < c):
        print(f'{b} is smallest!')
    else:
        print(f'{c} is smallest!')
