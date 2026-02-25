import sqlite3
import time

var=sqlite3.connect('dominos.db')

cor=var.cursor()
# name='YASHRAJ'
# password='yash'
# result=cor.execute('SELECT CNAME,PASSWORD FROM CUSTOMER WHERE CNAME=? AND PASSWORD =?',(name,password))
# print(list(result))

# cor.execute('CREATE TABLE CUSTOMER (CNAME VARCHAR (50),PASSWORD VARCHAR(8),MAILID VARCHAR2(20),MOBILENUM INTEGER (10))')

# cor.execute("INSERT INTO CUSTOMER VALUES ('YASHRAJ','yash@123','yash88@gmail.com',2345678991)")


# name='YASHRAJJJJ'
# o=cor.execute('SELECT CNAME FROM CUSTOMER WHERE CNAME=?',(name,))
# print(list(o))

# cor.execute('DROP TABLE PURCHASE')
# cor.execute('CREATE TABLE PURCHASE (CNAME VARCHAR (50),CARTVALUE INTEGER)')

# cor.execute("DROP TABLE IF EXISTS PURCHASE")

# cor.execute("""
# CREATE TABLE PURCHASE (
#     CNAME TEXT,
#     CARTVALUE INTEGER
# )
# """)

# cor.execute("INSERT INTO PURCHASE VALUES ('YASHRAJ',2000)")





menu_items = {
    "Veg": {
        "Margherita Pizza": 99,
        "Cheese n Corn Pizza": 169,
        "Peppy Paneer Pizza": 229,
        "Paneer Makhani Pizza": 249,
        "Veg Extravaganza Pizza": 299,
        "Farmhouse Pizza": 289,
        "Veggie Paradise Pizza": 259,
    },
    'Non-Veg':{
        'Barbeque Chicken Pizza' : 599
    }
    
    }

class Dominos:
    data={}
    food_items=None
    cart_value=0
    username=None

    
    @staticmethod
    def signup():
        while True :
            name=input("Enter the username :")
            password=input('Enter the password :')
            email=input("Enter the email :")
            mobilenum=int(input("Enter the mobilenumber :"))
          
            result=cor.execute('SELECT CNAME FROM CUSTOMER WHERE CNAME=?',(name,))
            result=list(result)
            if len(result)==0:
                if len(str(mobilenum))==10:
                    query=cor.execute('INSERT INTO CUSTOMER VALUES (?,?,?,?)',(name,password,email,mobilenum))
                    print('SIGNUP SUCESSFULLY!!!')
                    print('NOW WE CAN DO LOGIN')
                    Dominos.login()

                    break
                else:
                    print('MOBILE NUMBER IS NOT CORRECT')

            else:
                print('Username exist already ')

    @staticmethod
    def login():
        while True:
            name=input("Enter the username :")
            password=input('Enter the password :')
            result=cor.execute('SELECT CNAME,PASSWORD FROM CUSTOMER WHERE CNAME=? AND PASSWORD =?',(name,password))
            result=list(result)
            if len(result)!=0:
                print('LOGIN DONE!!!!!')
                Dominos.username=name
                Dominos.menu()
                break
            else:
                print('INVALID CREDITANIALS')
    
    @staticmethod
    def menu():
        def option(section):
            for items,price in (menu_items[section].items()):
                print(f'{items} : Rs {price}')
    
        print('PRESS 1 FOR VEG', '\n','PRESS 2 FOR NONVEG')
        i=int(input("ENTER YOUR CHOICE : "))
        if i==1:
            option('Veg')
            Dominos.food_items='Veg'
        else:
            option('Non-Veg')
            Dominos.food_items='Non-Veg'

        
        while True:
            options=input(('Press Y for exit and N for add more item :'))
            if options=='N':
                food=input("Enter the item :")
                if food not in Dominos.data:
                    Dominos.data[food]=1
                else:
                    Dominos.data[food]+=1
            else:
                print('ITEMS ADDED TO CART SUCESSFULLY')
                Dominos.cart()
                break

    @staticmethod
    def cart():
        print('----------------------------')
        print('-------CART SUMMARY----------')
        print('ITEMS                  PRICE       QUANTITY ')
        for i in Dominos.data:
            Dominos.cart_value+=Dominos.data[i] * menu_items[Dominos.food_items][i]
            print(
                i,
                Dominos.data[i] * menu_items[Dominos.food_items][i],
                Dominos.data[i]
            )
        print('Total cart value is  ',Dominos.cart_value)
        print('PRESS 1 FOR CHECKOUT AND 2 FOR ADD MORE ITEMS')
        j=int(input("Enter the option :"))
        if j==1:
            print('CHECKOUT DONE!!!')
            cor.execute("INSERT INTO PURCHASE VALUES  (?,?)",(Dominos.username,Dominos.cart_value))
            # print(Dominos.data)
        else:
            Dominos.data={}
            print('Cart is now empty')
            # print(Dominos.data)
            Dominos.menu()


    


Dominos.signup()





        


        
        

        


    
    

    


# Dominos.signup()
# Dominos.menu()
# Dominos.cart()

# Dominos.signup()










var.commit()
var.close()