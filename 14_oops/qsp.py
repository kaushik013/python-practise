

# class Company:

#     name = 'Google'
#     CEO = 'Ritesh agraval'
#     address = 'Ahmedabad'

# obj = Company()

# print(obj.name)
# print(Company.name)



# Company.name = 'Flipcart'
# print(obj.name)



# class School:

#     s_name = 'shree d.m. baarad'
#     loc = 'Talala'
#     staff = 32

# st = School()

# print(st.s_name)
# st.s_name = 'Aditya birla'
# st.loc = 'Veraval'
# st.staff = 50

# print(st.s_name)




# class School:
#     s_name = 'shree d.m. baarad'
#     loc = 'Talala'
#     staff = 32

# st = School()
# st.s_name = 'Aditya birla'
# st.loc = 'Veraval'
# st.staff = 50

# st1 = School()
# st1.name = 'kaushik'
# st1.age = 22
# st1.contact = 9016883191




# print(st.s_name,st.loc,st.staff)





# class Company:
#     # class properties
#     c_name='TCS'
#     Director='Bhavin'
#     Address='Ahemdabad'

# e1=Company()
# e1.name='kanji'
# e1.age=22
# e1.id=2
# e1.mail='kanji@123'

# e2=Company()
# e2.name='chetan'
# e2.age=20
# e2.id=3
# e2.mail='chetan@213'

# print(e1.name,e1.age,e1.id,e1.mail)
# # print(e2.name,e2.age,e2.id,e2.mail)

# #~ output:-
# """
# kanji 22 2 kanji@123
# chetan 20 3 chetan@213"""
# e1.age=25 # objecl property value update

# print(e1.name,e1.age,e1.id,e1.mail)
# #~ output:-
# """
# kanji 22 2 kanji@123
# kanji 25 2 kanji@123
# """


# ! __init__ 

# class School:

#     name = 'Shree D.M. barad'
#     loc = 'Talala'
#     CEO = 'Dhanabhai barad'


#     def __init__(self, name, age, address, contact, blood_grp):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.contact = contact
#         self.blood_grp = blood_grp

#     #!  ACCESSING 
#     def show(self):
#         print(self.name, self.age, self.address, self.contact,self.blood_grp)

#     #! MODIFY
#     def chang_blood_grp(self,new_bld):
#         self.blood_grp = new_bld
    
#     def change_age(self, new_age):
#         self.age = new_age


#     #! Accessing class member
#     @classmethod
#     def access(cls):
#         print(cls.name, cls.loc, cls.CEO)


#     #! Modify class member   
#     @classmethod
#     def chg_ceo(cls,new_ceo):
#         cls.CEO = new_ceo
    
    



# obj = School('kaushik',22,'ahmedabad',9016883191,'B+')
# School.access()
# School.chg_ceo('Yashraj')
# School.access()


# # obj.show()
# # obj.chang_blood_grp('O+')
# # obj.change_age('25')
# # obj.show()



#! create a class company which consist of three class member along with 2 objects with each for object member

# class Company:

#     name = 'infosys'
#     loc = 'Mumbai'
#     ceo = 'yashrajsir'


#     def __init__(self, name, age, sallery, dept):
#         self.name = name
#         self.age = age
#         self.sallery = sallery
#         self.dept = dept


# emp1 = Company('kaushik',22,50000,'IT')
# print('company name is : ',Company.name)
# print(emp1.name,emp1.age,emp1.sallery,emp1.dept)
# print()

# emp2 = Company('Raj',21,10000,'Account')
# print('company name is : ',Company.name)
# print(emp2.name,emp2.age,emp2.sallery,emp2.dept)



# ! create a class Bank with 3 class member, 4 object, 3 object member, two class method and two object method 



class Bank:

    #^ class member
    name = 'HDFC Bank'
    loc = 'Ahmedabad'
    BM = 'Ashok desai'

    #^ cunstructor
    def __init__(self, c_name, acc_no, balance, contact):
        self.c_name = c_name
        self.acc_no = acc_no
        self.balance = balance
        self.contact = contact

    #^ object method (access)
    def show_details(self):
        print('\n\nBank name :',self.name,)
        Bank.greet()
        print('Customer name : ',self.c_name)
        print('Account no : ',self.acc_no)
        print('Balance : ',self.balance)
        print('Contact : ',self.contact)
    
    #^ object method (change)
    def cnj_contact(self,new_contact):
        self.contact = new_contact
    

    #^ class method (access)
    @classmethod
    def show_cls(cls):
        print('Bank : ',cls.name)
        print('Address : ',cls.loc)
        print('BM : ',cls.BM)

    #^ class method (modify)
    @classmethod
    def cng_bm(cls,new_BM):
        Bank.BM = new_BM

    #^ staticmethod 
    @staticmethod
    def greet():
        print('hello how are you!')

#! object 1
per1 = Bank('Rahul',98231 ,90000, 9016848448)
per1.show_details()
per1.cnj_contact(9089787889)
per1.show_cls()
per1.cng_bm('Rajesh shah')

#! object 2
per2 = Bank('Kabir',98232 ,100000, 9359493933)
per2.show_details()
# per2.cnj_contact(9085453433)
# per2.show_cls()
# per1.cng_bm('Raj malhotra')

#! object 3
per2 = Bank('Jaydeep',99084 ,120000, 935949394)
per2.show_details()
# per2.cnj_contact(9085453443)
# per2.show_cls()
# per1.cng_bm('Sanjay pathak')


#! object 4
per2 = Bank('Dharmesh',98235 ,150000, 9359493435)
per2.show_details()
# per2.cnj_contact(9085453453)
# per2.show_cls()
# per1.cng_bm('Abhishek gupta')
