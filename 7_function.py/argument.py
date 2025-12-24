
#! types of argument 

# positional argument
# default argument
# keyword argument
# variable length agrument


def info(name,mail,contact,altercontact=None):
    print(f'name is {name}')
    print(f'mail is {mail}')
    print(f'contact is {contact}')
    print(f'altercontact is {altercontact}')


# info('kaushik','chariyakaushik13@mail.com',9016883191)  
# info('janvi','janvi2003@mail.com',8200134221,9013747833)


#! keyword argument


def info(**kwargs):
    print(type(kwargs))
    print(kwargs)

# info(a=12,b=13,c=14)



#! variable length agrument


def pack(*t,**d):
    print(type(t))
    print(t)
    print(type(d))
    print(d)

# pack(12,131,141,115,15,d = 12,g= 13)


def extract_vowel(n,vowel = ''):
    for i in n:
        if i in 'AEIOUaeioy':
            vowel += i
    return vowel

# a = input('enter the str : ')
# print(extract_vowel(a))


a = 10
def demo():

    a = 20
    print(a)
    print('hii')
demo()
