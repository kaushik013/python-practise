

# ⁡⁢⁣⁢elif condition ⁡
# ⁡⁢⁣⁣1. Check if a number is positive, negative, or zero.
# 2. Check if a person is a child (age < 13), teenager (13-19), or adult (20+). 
# 3. Check the grade of a student based on marks (A, B, C, D, or Fail). 
# 4. Check if a day is a weekday or weekend based on input. 
# 5. Check if a given month number belongs to Winter, Summer, or Monsoon. 
# 6. Check if a temperature is cold (<15°C), moderate (15-30°C), or hot (>30°C). 
# 7. Check if a number is single-digit, double-digit, or more. 
# 8. Check if a person’s weight category is underweight, normal, or overweight. 
# 9. Check if an input character is a vowel, consonant, or other symbol. 
# 10. Check if a number is divisible by 2, 3, or neither. 
# 11. Check if an employee’s salary falls into Low (<30K), Medium (30K-60K), or High 
# (>60K). 
# 12. Check if a triangle is Equilateral, Isosceles, or Scalene. 
# 13. Check the size of a T-shirt (S, M, L, XL) based on input. 
# 14. Check if a given input is an alphabet, number, or special character. 
# 15. Check if a train ticket is Economy, Business, or First Class.⁡


# 1. Check if a number is positive, negative, or zero

# a = int(input('enter the number : '))

# if(a > 0):
#     print('number is positive number!')
# elif(a < 0):
#     print(f'number is nagative number!')
# elif(a == 0):
#     print(f'number is zero!')
# else:
#     print('not a number!')




# 2. Check if a person is a child (age < 13), teenager (13-19), or adult (20+). 

# age = int(input('enter your age : '))

# if(age < 13):
#     print('you are child!')
# elif(age >= 13 and age <= 19):
#     print('you are teen!')
# else:
#     print('you are adult!')




# 3. Check the grade of a student based on marks (A, B, C, D, or Fail). 

# math = int(input('enter marks : '))
# phy = int(input('enter marks : '))
# bio = int(input('enter marks : '))
# chem = int(input('enter marks : '))
# eng = int(input('enter marks : '))


# total = math + phy + bio + chem + eng
# per = total // 5

# if(math >= 33 and phy >= 33 and bio >= 33 and chem >= 33 and eng >= 33):
#     if(per >= 90):
#         print('A grade!')
#     elif(per >= 80):
#         print('B grade!')
#     elif(per >= 70):
#         print('C grade!')
#     elif(per >= 33):
#         print('D grade!')
# else:
#     print('you are fail!')



# 4. Check if a day is a weekday or weekend based on input. 

# a = input('Enter a day : ')

# if(a in ['monday','tuesday','wednesday','thursday','friday','saturday',]):
#     print(f'{a} is weekday!')
# elif(a == 'sunday'):
#     print(f'is sunday!')
# else:
#     print('not a day!')


# 5. Check if a given month number belongs to Winter, Summer, or Monsoon. 

# a = int(input('enter the month  1 to 12 : '))

# if(a in [12,1,2]):
#     print('Winter 🥶')
# elif(a in [3,4,5,6]):
#     print('Summer 🥵')
# else:
#     print('Monsoon 🌧️')




# 6. Check if a temperature is cold (<15°C), moderate (15-30°C), or hot (>30°C). 

# a = int(input('enter the temperature : '))

# if(a < 15):
#     print('cold 🥶')
# elif(a >= 15 and a <= 30):
#     print('moderate')
# else:
#     print('hot 🔥')



# 7. Check if a number is single-digit, double-digit, or more. 

# a = int(input('enter the number : '))

# if(a >= 0 and a<= 9):
#     print(f'{a} is single digit!')
# elif(a >= 10 and a <= 99):
#     print(f'{a} is two digit!')
# else:
#     print('triple-digit, or more !')



# 8. Check if a person’s weight category is underweight, normal, or overweight. 

# a = float(input('enter the weight : '))

# if(a <= 40):
#     print(f'{a}kg is underweight ')
# elif(a > 40 and a <= 60):
#     print(f'{a}kg is normal weight')
# else:
#     print(f'{a}kg is overweight')



# 9. Check if an input character is a vowel, consonant, or other symbol. 

# a = input('enter the character !')

# if(a in 'AEIOUaeiou'):
#     print(f'{a} is vowel character!')
# elif(a >= 'A' and a <= 'Z' or a >= 'a' and a <= 'z'):
#     print(f'{a} is consonant!')
# else:
#     print(f'{a} is special character!')
    



# 10. Check if a number is divisible by 2, 3, or neither. 

# a = int(input('enter the number : '))

# if(a % 2 == 0):
#     print(f'{a} is divisable by 2')
# elif(a % 3 == 0):
#     print(f'{a} is divisable by 3')
# else:
#     print('not divisable!')




# 11. Check if an employee’s salary falls into Low (<30K), Medium (30K-60K), or High (>60K).

# sal = int(input('enter the sallery : '))

# if(sal <= 30):
#     print('Low!')
# elif(sal > 30 and sal <= 60):
#     print('Medium')
# else:
#     print('high')




# 12. Check if a triangle is Equilateral, Isosceles, or Scalene.

# a = int(input('enter the side 1 : '))
# b = int(input('enter the side 2 : ')) 
# c = int(input('enter the side 3 : ')) 

# if(a == b == c):
#     print('Equilateral trangle')
# elif(a == b or a == c or b == c):
#     print('Isosceles trangle')
# else:
#     print('Scalene trangle')



# 13. Check the size of a T-shirt (S, M, L, XL) based on input. 

# size = input('enter the t-shirt size : ')

# if(size == 'S' or size == 's'):
#     print('small')
# elif(size == 'M' or size == 'm'):
#     print('medium')
# elif(size == 'L' or size == 'l'):
#     print('long')
# else:
#     print('XL')




# 14. Check if a given input is an alphabet, number, or special character. 

# a = input('enter the input : ')

# if(a.isalpha()):
#     print(f'{a} is string')
# elif(a.isdigit()):
#     print(f'{a} is digit')
# else:
#     print('special character')



# 15. Check if a train ticket is Economy, Business, or First Class.

# a = input('enter the tickit : ')

# if(a == 'E' or a == 'e'):
#     print('Economy ticket')
# elif(a == 'B' or a == 'b'):
#     print('Business class ticket')
# elif(a == 'F' or a == 'f'):
#     print('First Class ticket')
# else:
#     print('invalid ticket')



