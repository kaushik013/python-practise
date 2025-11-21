

# ⁡⁣⁣⁡⁣⁣⁢if else condition⁡

# it help your code run different block depending on whether is condition is True or False


# ⁡⁢⁣⁣Syntax :-⁡

# if(condition):
    #   print('code to run if condition is True')
# else:
    #  print('code to run if condition is False')


# ⁡⁣⁣⁢example⁡
age = 18
if(age >= 18):
    print('You can vote')
else:
    print('Cant vote')


# ⁡⁣⁣⁢if elif else⁡

mark = 32

if(mark >= 90):
    print('your have A grade')
elif(mark >= 80):
    print('you have grade B')
elif(mark >= 33 and mark <= 70):
    print('your score id c')
elif(mark <= 33):
    print('you are fail')
else:
    print('so')



# ⁡⁣⁣⁢nested if else ⁡

num = 1

if(num > 0):
    if(num % 2 == 0):
        print('positive Even number')
    else:
        print('positive odd number')
else:
    print('nagative number')


# ⁡⁣⁣⁢sort hand if else (one line)⁡

x = 5
print('big') if(x > 3) else print('small')



# ⁡⁣⁣⁢check temprature⁡
temprature = 36

if(temprature > 35):
    print('hot temprature!')
elif(temprature > 25):
    print('midume temprature!')
else:
    print('cold temprature')


# ⁡⁣⁣⁢with logical operator⁡

year = int(input('enter year : '))

if(year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print('leap year')
else:
    print('not leap year')



amount = float(input('Enter your amount : '))

if(amount >= 5000):
    discount = amount * 0.20
elif(amount >= 4000):
    discount = amount * 0.10
elif(amount >= 2500):
    discount = amount * 0.05
elif(amount >= 1):
    discount = amount * 0
    print('Sugar free!')
else:
    ('soping more 🛒')

print('discount is ',discount)
print('total amount pay : ',amount - discount)


# ⁡⁣⁣⁢chech digit or alpha⁡

char = input('enter character : ')

if(char.isdigit()):
    print(char,'id digit')
elif(char.isalpha()):
    print(char,'is alpha')
else:
    print(char,'is special character')


password = input('Enter password : ')

if(password[0].isupper() and password.isalnum() for ch in password):
    print('Password strong')
else:
    print('Password week')


a = (1,2,3)

print(type(a))

# ⁡⁣⁣⁢check num multiple by 3 or 7⁡

nums = int(input('Enter your number : '))

if(nums % 3 == 0 and nums % 7 == 0):
    print(nums,'multiply by 3 or 7') 
else:
    print(nums,'not a mulyiply by3 , 7')




# ⁡⁣⁣⁢is between 10 to 50⁡
inp = int(input('Enter your number : '))

if(inp >= 10 and inp <= 50):
    print(inp,'is between 10 to 50')
else:
    print(inp,'not between 10 to 50')




# Input three sides of the triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

#⁡⁣⁣⁢ Check for triangle type⁡
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")



# ⁡⁣⁣⁢password⁡
password = input("Enter your password: ")

if password.startswith('A') and any(ch.isdigit() for ch in password) and len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
