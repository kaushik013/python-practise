

#! excapction handling 

#! 1. specific excepction handling 

# syntax 

# try : 
#     program

# except errorname :
#     soluction


# while True : 
#     try :
#         a = int(input('enter the num : '))
#         b = int(input('enter the num : '))
#         print(a/b)
#         break

#     except ValueError:
#         print('please enter only int datatype')

#     except ZeroDivisionError : 
#         print('can not divided by 0 ')



#! 2. generic excepction handling 

# syntax 

# try : 
#     program

# except Exception as var_name :
#     soluction 


# while True:

#     try:
#         a = int(input('enter the num : '))
#         b = int(input('enter the num : '))
#         print(a/b)
#         break
    
#     except Exception as error :
#         print('error is  : ', error)


# syntax 

    # try : 
    #     program

    # except :
    #     soluction



#! 3. default excepction handling 


while True:

    try:
        a = int(input('enter the num : '))
        b = int(input('enter the num : '))
        print(a/b)
        break
    
    except Exception as error :
        print('error is  : ', error)

    except KeyboardInterrupt:
        print('except KeyboardInterrupt error')

