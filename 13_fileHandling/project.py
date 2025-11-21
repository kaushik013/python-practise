
from pathlib import Path
import os




def allfileread():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f'{i} : {items}')


def createfile():
    name = input('enter your file name : ')
    file = Path(name)
    if(file.exists()):
        write = input('enter contant to add appdend : ')
        with open(name,'a')as fs:
            fs.write('  '+ write)
            print('text is added! ✅')
    else:        
        with open(name,'w')as fs:
            write = input('enter content : ')
            fs.write(write)
            print('file created successful! ✅')


def readfile():
    allfileread()
    name = input('enter file name for read :-')
    file = Path(name)
    if(file.exists()):
        with open(name,'r')as fs:
            print(fs.read())
    else:
        print('not exist file ❌')   
        print('you want to create file yes & no')
        create = input('enter yes or no! : ')
        if(create == 'yes'):
            with open(name,'w')as fs:
                write = input('enter content : ')
                fs.write(write)
                print('file created successful! ✅')
        else:
            print('thank you 😊 !')



def updatefile():
    allfileread()
    name = input('enter file name you want update : ')
    file = Path(name)
    if(file.exists()):
        print('you want to file override or append')
        opction = int(input('you want to override press 1 aapend press 2 : '))
        if(opction == 1):
            with open(name,'w')as fs:
                write = input('enter contenrt you want to override : ')
                fs.write(write)
                print('your content is overrided! ✅')
        elif(opction == 2):
            with open(name,'a')as fs:
                write = input('enter contenrt you want to override : ')
                fs.write(' ' +write)
                print('your content is added! ✅')
        else:
            print('invalid input! ❌')
    else:
        print('file not exist!')
        print('you want to add file press yes or no ')

        create = input('enter yes or no! : ')

        if(create == 'yes'):
            with open(name,'w')as fs:
                write = input('enter content : ')
                fs.write(write)
                print('file created successful! ✅')
        else:
            print('thank you 😊 !')




def deleting():
    name = input('enter file name which you want to delate : ')
    file = Path(name)
    if(file.exists()):
        file.unlink()
        print(f'{name} file is deleted! ✅')
    else:
        print('file not exist! ❌') 


def renamefile():
    allfileread()
    name = input('enter file name for rename : ')
    file = Path(name)
    if(file.exists()):
        new = input('enter your new name : ')
        os.rename(name,new)
        print(f'{name} file name updated! ✅')
        print(f'{new} file name updated! ✅')
    else:
        print('file not exist! ❌')



print('enter 1 for creating file!')
print('enter 2 for read file!')
print('enter 3 for update file!')
print('enter 4 for delate file!')
print('enter 5 for update file name')

check = int(input('chhose opction : '))




if(check == 1):
    allfileread()
    createfile()

if(check == 2):
    readfile()

if(check == 3):
    updatefile()

if(check == 4):
    deleting()

if(check == 5):
    renamefile()