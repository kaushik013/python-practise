

# dictionary

#  ⁡⁢⁣⁣Definition⁡
#⁡⁣⁢⁣ it is a collection of key value pair⁡
# ⁡⁣⁢⁣Each value is accessed using its key, not an index.⁡


# ⁡⁢⁣⁢Syntax⁡

my_dict = {
    'name' : 'janvi',
    'stream' : 'cs',
    'age' : 21,
    'city' : 'ahm'
}


# ⁡⁢⁣⁣empty dict⁡

a = {}
print(type(a))
# <class 'dict'>



# ⁡⁢⁣⁣ditionary power⁡

# ⁡⁢⁣⁡⁢⁣⁣mutable ⁡⁣⁢⁣-- > it means you can change the value after creation⁡ ⁡⁣⁢⁣like add, remove⁡



# ⁡⁢⁣⁣how to access values⁡
a = {10:100,20:200,30:300,40:400,50:500}

print(a[20])
# 200


# ⁡⁢⁣⁣how to change the value⁡

a[50] = 5000
print(a)
# {10: 100, 20: 200, 30: 300, 40: 400, 50: 5000}



# ⁡⁢⁣⁡⁣⁣⁢looping in dict ⁡

c = {1:11,2:12,3:13,4:14,5:15}


# ⁡⁣⁣⁢access key⁡
for key in c:
    print(key)

# ⁡⁣⁣⁢access value⁡
for val in c.values():
    print(val)

# ⁡⁣⁣⁢access key and value both⁡
for key,val in c.items():
    print(key,val)


# ⁡⁣⁣⁢marge two number⁡
a = {1:11,2:12,3:13,4:14,5:15}
b = {5:15,6:16,7:17,8:18,9:19}

for i in b:
    a[i] = b[i]
print(a)



# ⁡⁣⁣⁢deep copy ⁡

a = {'a':10,'b':20,'c':30}

b = a
b['a'] = 100
print(b)
print(a)
# {'a': 100, 'b': 20, 'c': 30}  ⁡⁢⁣⁢note⁡ :-⁡⁢⁣⁣ we can change in b but actual change in⁡ ⁡⁢⁣⁣a⁡


# ⁡⁣⁣⁢shelo copy⁡ 

a = {'a':10,'b':20,'c':30}
b = a.copy()

b['a'] = 1000

print(b)  # {'a': 1000, 'b': 20, 'c': 30}
print(a)  # {'a': 10, 'b': 20, 'c': 30}

# ⁡⁢⁣⁢note⁡ :-⁡⁢⁣⁣ we can change in b but not change in⁡ ⁡⁢⁣⁣a ⁡⁢⁣⁣in shello copy⁡⁡



# ⁡⁣⁣⁢inbuilt method in dict⁡

# ⁡⁢⁣⁣update()⁡
# ⁡⁣⁢⁣it is used to add key and value

a = {
    1:10,
    2:20,
    3:30
}

a.update({4:40})
print(a)
# {1: 10, 2: 20, 3: 30, 4: 40}

# ⁡⁢⁣⁢OR⁡ 

a[5] = 50
print(a)
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}



# ⁡⁢⁣⁣del⁡ 
# --> ⁡⁣⁢⁣delete key value pair⁡


c = {1:11,2:12,3:13}
del c[3]
print(c)
# {1: 11, 2: 12}


# ⁡⁢⁣⁣get()⁡
# ⁡⁣⁢⁣Returns value of key (or None if not found)⁡

a = {1:11,2:22,3:33}

print(a.get(1))
# 11


# ⁡⁢⁣⁣keys()⁡
#⁡⁣⁢⁣ Returns all keys⁡

keys = {
    'key1' : 'val1',
    'key2' : 'val2',
    'key3' : 'val3',
    'key4' : 'val4',
    'key5' : 'val5'

}

print(keys.keys())
# dict_keys(['key1', 'key2', 'key3', 'key4', 'key5'])


# ⁡⁢⁣⁣values()⁡
# ⁡⁣⁢⁣Returns all values⁡

keys = {
    'key1' : 'val1',
    'key2' : 'val2',
    'key3' : 'val3',
    'key4' : 'val4',
    'key5' : 'val5'
}

print(keys.values())
# dict_values(['val1', 'val2', 'val3', 'val4', 'val5'])


# ⁡⁢⁣⁣item()⁡
# ⁡⁣⁢⁣Returns all key-value pairs⁡

keys = {
    'key1' : 'val1',
    'key2' : 'val2',
    'key3' : 'val3',
    'key4' : 'val4',
    'key5' : 'val5'
}

print(keys.items())
# dict_items([('key1', 'val1'), ('key2', 'val2'), ('key3', 'val3'), ('key4', 'val4'), ('key5', 'val5')])


#⁡⁢⁣⁣ pop()⁡
# ⁡⁣⁢⁣Removes item by key⁡

keys = {
    'key1' : 'val1',
    'key2' : 'val2',
    'key3' : 'val3',
    'key4' : 'val4',
    'key5' : 'val5'
}

print(keys.pop('key5'))
# val5


# ⁡⁢⁣⁣clear()⁡
# ⁡⁣⁢⁣Clears the dictionary⁡

keys = {
    'key1' : 'val1',
    'key2' : 'val2',
    'key3' : 'val3',
    'key4' : 'val4',
    'key5' : 'val5'
}

print(keys.clear())
# None



