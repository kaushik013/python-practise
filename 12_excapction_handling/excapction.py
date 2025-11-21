

# ⁡⁢⁣⁣excapction handling ⁡

# ⁡⁣⁢⁣Exception Handling is a way to manage errors that occur during program execution — 
# instead of stopping the whole program, Python lets you handle the error smoothly

# ⁡⁢⁣⁡⁣⁣⁢Exception ⁡                ⁡⁣⁣⁢Type Meaning⁡

# ⁡⁢⁣⁣ZeroDivisionError⁡	     ⁡⁣⁢⁣Division by zero⁡
# ⁡⁢⁣⁣ValueError⁡ 	            ⁡⁣⁢⁣ Wrong data type⁡
# ⁡⁢⁣⁣TypeError	  ⁡              ⁡⁣⁢⁣Operation on wrong type⁡
# ⁡⁢⁣⁣IndexError⁡	             ⁡⁣⁢⁣List index out of range⁡
# ⁡⁢⁣⁣KeyError	⁡               ⁡⁣⁢⁣ Key not found in dictionary⁡
# ⁡⁢⁣⁣FileNotFoundError⁡	     ⁡⁣⁢⁣File doesn’t exist⁡



# ⁡⁢⁣⁣basics syntax⁡

# try:
     # code that may raise an exception
# except ExceptionType:
     # code to handle the exception
# else:
     # runs if no exception occurs
# finally:
     # always runs (cleanup)




a = int(input('enter your number : '))

try:
    print(10/a)
except Exception as error:
    print(f'❌ error is a  = {error}')
else:
    print('i have no error ✅')
finally:
    print('no matter what it is always run')



age = int(input('enter your age : '))

try:
    if(age < 10 or age > 18):
        raise ValueError('your age is not should be between 18 and 10')
    else:
        print('welcome ')

except Exception as error:
    print(f'your error is {error}')

print('execute ✅')



try:
    num = int(input('Enter your number : '))

    result = 10 / num

except ZeroDivisionError:
    print('cannot devide by zero')
except ValueError:
    print('invalid input')
else:
    print('division successful',result)
finally:
    print('program finished!')



try:
    a = [1, 2, 3]
    print(a[5])  # index out of range
except Exception as e:
    print("⚠️ An error occurred:", e)
