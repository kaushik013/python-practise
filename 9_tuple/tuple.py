

# ⁡⁣⁣⁢what is tuple ?⁡
# ---> ⁡⁣⁢⁣touple is collection of a item(like a list)⁡

# ⁡⁢⁣⁢Note : tupple is immutable (we can not change the value and remove and add )⁡

#
# Syntax :-

# touple_name = (item1,item2,item3) 

# example :-

tupple = (1,2,3,4,5)
print(type(tupple))
# <class 'tuple'>


# ⁡⁣⁣⁢Feature⁡           	                                ⁡⁣⁣⁢Description⁡

# ⁡⁢⁣⁣Ordered   ⁡        	                                ⁡⁣⁢⁣Items have a defined order⁡
# ⁡⁢⁣⁣Immutable	⁡                                           ⁡⁣⁢⁣Cannot be changed after creation⁡
# ⁡⁢⁣⁣Allow Duplicates⁡	                                    ⁡⁣⁢⁣Same values can appear multiple times⁡
# ⁡⁢⁣⁣Can contain different data types⁡	                  ⁡⁣⁢⁣  Yes⁡


data = (11,22,33,44,55,22)

# tupple can allow single value like this 

my_tpl1 = {1} # ---> not like this ⁡⁣⁢⁢⁡⁢⁣⁢this is a int not tupple⁡
print(type(my_tpl1))  # # <class 'int' >


my_tpl = {1,} # ---> this is a tuple
print(type(my_tpl))  # # <class 'tuple' >








# ⁡⁢⁣⁣inbuilt method⁡

# index()

# it is used to return the index of perticular element 

# ⁡⁣⁣⁢syntax:-⁡
# var.index(val)

print(data.index(22))
# 1



# ⁡⁣⁣⁢count()⁡
# it is used to count the existing element 

#⁡⁣⁣⁢ syntax:-
# var.count(value)

mark = (22,43,54,65,45,53,22)
print(mark.count(22))
# 2

