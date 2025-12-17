

# ⁡⁣⁣⁢what if function⁡ ?

# ---> ⁡⁣⁢⁣function is a block of code that perform specific task⁡
 
# It helps in code ⁡⁢⁣⁣reusability, organization,⁡ and ⁡⁢⁣⁣clean⁡ structure.

# ⁡⁣⁣⁢why used function

# ✅ ⁡⁢⁣⁣to make a code reusable⁡
# ✅ ⁡⁢⁣⁣to make a code organized and readble⁡
# ✅ ⁡⁢⁣⁣to make a code easy to debug nd maintain
# ✅ ⁡⁢⁣⁣to avoid repetition⁡



# type of function 

# built in function --> already declare in python

# example --> print(), len(), max(), sum()

# ⁡⁢⁣⁢User-defined Functions – Created by the user using⁡ ⁡⁢⁣⁣def⁡.

# ⁡⁢⁣⁣Sytax⁡

# def function_syntax(parameter):
    # block code 
    # return value


#//! types of argument

#//!^ 1. positional argument
# //^ 2. default argument
# //^ 3. Keyword argument 
# //^ 4. Variable Length Arguments (*args)
# //^ 5. Keyword Variable Length Arguments (**kwargs)




def hello():
    print('this is a hello function')
hello()




# ⁡⁢⁣⁣Argument

# 1. ⁡⁣⁣⁢positional argument⁡

def name(a,b):
    print(a,b) # <--- ⁡⁢⁣⁣positional arg⁡
name('kaushik','chariya')


# ⁡⁣⁣⁢2. ⁡⁣⁣⁢keyword argument⁡

def movie(movie,hero):
    print(f'movie is {movie} and is hero is {hero}')
movie(hero='tiger',movie='badhi 4')


# ⁡⁣⁣⁢3. default argument⁡

def fruits(a = 'graps', b = 'banana'):
    print(f'{a} {b}')
fruits('banana','apple')

