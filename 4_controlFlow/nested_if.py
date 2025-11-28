

# ⁡⁢⁣⁣1. Check if a number is positive, then check if it's even or odd. 
# 2. Check if a number is negative, then check if it's a multiple of 5. 
# 3. Check if a person is eligible to vote, then check if they are a senior citizen. 
# 4. Check if a number is greater than 50, then check if it's divisible by 10. they are a senior citizen
# 5. Check if a given character is an alphabet, then check if it's uppercase or lowercase. 
# 6. Check if a student has passed, then check if they scored distinction (>=75). 
# 7. Check if a year is a leap year, then check if it is a century year. 
# 8. Check if a person is eligible for a discount, then check if the purchase is above 10,000.  
# 10. Check if a person’s age is above 18, then check if they can drive a car. 
# 11. Check if an entered username is correct, then check if the password is correct. 
# 12. Check if a triangle is valid, then check if it's equilateral, isosceles, or scalene. 
# 13. Check if a student passed, then check if they got a scholarship (>90 marks). 
# 14. Check if a person is tall, then check if they are also underweight. 
# 15. Check if a number is within a range, then check if it is odd or even. 
# 16. Check if a product is in stock, then check if it is on sale. 
# 17. Check if a bank account balance is sufficient, then check if withdrawal is possible. 
# 18. Check if a given input is a number, then check if it's positive or negative.⁡



# ⁡⁢⁣⁣1. Check if a number is positive, then check if it's even or odd. 

# a = int(input('enter the number : '))

# if(a >= 0):
#     if(a % 2 == 0):
#         print('even number ')
#     else:
#         print('odd number')
# else:
#     print('nagative number')




# 2. Check if a number is negative, then check if it's a multiple of 5. 

# a = int(input('enter the number : '))

# if(a <= 0):
#     if(a % 5 == 0):
#         print('multiple by 5 ✅')
#     else:
#         print('not multiple by 5 ❌')
# else:
#     print('not nagative number ')



# 3. Check if a person is eligible to vote, then check if they are a senior citizen. 

# age = int(input('enter the age : '))

# if(age >= 18):
#     print('eligible to vote ✅')
#     if(age >= 45):
#         print('they are a senior citizen 👨🏻‍🦼‍➡️')
#     else:
#         print('they are not a senior citizen ❌')
# else:
#     print('not eligible to vote ❌')



# 4. Check if a number is greater than 50, then check if it's divisible by 10. 

# num = int(input('enter the number : '))

# if(num >= 50):
#     if(num % 10 == 0):
#         print("it's divisible by 10 ✅")
#     else:
#         print("it's not divisible by 10 ❌")
# else:
#     print('number are not grater than 50 ❌')



# 5. Check if a given character is an alphabet, then check if it's uppercase or lowercase. 

# a = input('enter the character : ')

# if(a.isalpha()):
#     if(a.isupper()):
#         print(f'{a} is uppercase')
#     else:
#         print(f'{a} is lower')
# else:
#     print('not a alpha character ❌')



# 6. Check if a student has passed, then check if they scored distinction (>=75). 


# math = int(input('enter marks : '))
# phy = int(input('enter marks : '))
# bio = int(input('enter marks : '))
# chem = int(input('enter marks : '))
# eng = int(input('enter marks : '))


# total = math + phy + bio + chem + eng
# per = total // 5

# if(math >= 33 and phy >= 33 and bio >= 33 and chem >= 33 and eng >= 33):
#     if(per >= 75):
#         print('yes 75 up! ✅')
#     else:
#         print('not 75 up! ❌')
# else:
#     print('you are fail! 😕')




# 7. Check if a year is a leap year, then check if it is a century year. 

# year = int(input('enter the year! : '))

# if((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)):   
#     if(year % 400 == 0):
#         print('it is a century year ✅')
#     else:
#         print('only leap year! ✅')
# else:
#     print('not leap year ❌')




# 8. Check if a person is eligible for a discount, then check if the purchase is above 10,000.  


# buy = int(input('enter the purchase amount : '))

# if(buy >= 5000):
#     print('person is eligible for a discount ✅')
#     if(buy >= 10000):
#         print('the purchase is above 10,000 ✅')
#     else:
#         print('the purchase is not above 10,000 ❌')
# else:
#     print('person is not eligible for a discount ❌')



# 10. Check if a person’s age is above 18, then check if they can drive a car. 

# age = int(input("Enter your age: "))

# if age > 18:
#     print("You are eligible. You can drive a car 🚗")
# else:
#     print("You are not eligible to drive a car ❌")



# 11. Check if an entered username is correct, then check if the password is correct. 

# user = 'Kaushik_13'
# password = 'Kaushik@13'

# id = input('enter the user : ')

# if(id == user):
#     pash = input('enter password : ')
#     if(pash == password):
#         print('login sucessfully! ✅ ')
#     else:
#         print('password is not valid! ❌')
# else:
#     print('id is not valid! ❌')



# 12. Check if a triangle is valid, then check if it's equilateral, isosceles, or scalene. 

# a = int(input('enter the triangle 1 : '))
# b = int(input('enter the triangle 2 : '))
# c = int(input('enter the triangle 3 : '))


# if(a + b > c and c + a > b and b + c > a):
#     if(a == b == c):
#         print('equilateral trangle!')
#     elif(a == b or a == c or b == c):
#         print('isosceles trangle!')
#     else:
#         print('scalene trangle!')
# else:
#     print('not a valid trangle ❌')





# 13. Check if a student passed, then check if they got a scholarship (>90 marks). 



# math = int(input('enter marks : '))
# phy = int(input('enter marks : '))
# bio = int(input('enter marks : '))
# chem = int(input('enter marks : '))
# eng = int(input('enter marks : '))


# total = math + phy + bio + chem + eng
# per = total // 5

# if(math >= 33 and phy >= 33 and bio >= 33 and chem >= 33 and eng >= 33):
#     if(per >= 90):
#         print('they got a scholarship ✅')
#     else:
#         print('they cannot eligible for scholarship ❌')
# else:
#     print('you are fail! 😕')





# 14. Check if a person is tall, then check if they are also underweight. 

# height = int(input('enter the height : '))
# weight = int(input('enter the weight : '))

# if(height > 170):
#     if(weight < 50):
#         print('they are also underweight')
#     else:
#         print('they are also tall but not underweight 😕')
# else:
#     print('a person is  not tall ❌')




# 15. Check if a number is within a range, then check if it is odd or even. 

# num = int(input('enter the number : '))

# if(num >= 50 and num <= 100):
#     if(num % 2 == 0):
#         print('it is even !')
#     else:
#         print('it is odd !')
# else:
#     print('not a range between 50 - 100')




# 16. Check if a product is in stock, then check if it is on sale. 


# customer = input('you have stock in this product yes / no : ')

# if(customer == 'yes'):
#     sale = input('this product on sale yes / no : ')
#     if(sale == 'yes'):
#         print('Product is in stock and on sale!')
#     else:
#         print('product in stock but we cant sale it!')
# else:
#     print('not i stock!')





# 18. Check if a given input is a number, then check if it's positive or negative.⁡


# a = eval(input('enter the input : '))

# if (type(a) == int):
#     if(a >= 0):
#         print('positive number!')
#     else:
#         print('nagative number!')
# else:
#     print('not a number ')





# 17. Check if a bank account balance is sufficient, then check if withdrawal is possible. 


balance = 10000
ATM_PIN = 1213

pas = int(input('enter your bank PIN for check balance : '))

if(pas == ATM_PIN):
    print(balance)

    amount = int(input('enter your amount for widrow! : '))

    if(balance >= amount):
        print('withdraw is possible! ✅')

        yes = input('you want to widrow ? yes / no : ')
        if(yes == 'yes'):
            widrow = int(input('enter ATM pin : '))

            if(widrow == ATM_PIN):
                balance -= amount
                print(f'sucesfully withdraw amount {amount}Rs.')
                check = input('press "yes" for check bank balance! : ')

                if(check == 'yes'):
                    PIN = int(input('enter your bank password for check balance : '))

                    if(PIN == ATM_PIN):
                        print(f'{balance}Rs your balance!')
                        print('thanl you 😊')

                    else:
                        print('pin incorrect! ❌')

                else:
                    print('thank you 😊')

            else:
                print('incorrect PIN! ❌')

        else:
            print('thank you 😊')

    else:
        print('not possible your balanse is down ❌')
        
else:
    print('incorrect password! ')