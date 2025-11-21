

# definition

# ⁡⁣⁢⁣set is a unique and unored list in python⁡


# ⁡⁢⁣⁣It removes duplicate values automatically
# The order of elements is not fixed (no indexing)⁡

# ⁡⁣⁣⁢syntax :-⁡

# var = {val1,val2,val3....valn}


# ⁡⁣⁣⁢set power⁡
# ⁡⁢⁣⁣set is a mutable data type⁡

# ⁡⁢⁣⁣duplicate value cannot allowed⁡

# ⁡⁢⁣⁣set are unordered list we cant access it⁡

# ⁡⁢⁣⁣set is semi-hetrogonus like accept string, number, tuple nor everything⁡


# ⁡⁢⁣⁢set method()⁡


# ⁡⁢⁣⁣add()
#⁡⁣⁢⁣ it is used to add element in last ⁡

a = {1,2,3,4,5}
a.add(6)
print(a)

# {1, 2, 3, 4, 5, 6}


# ⁡⁢⁣⁣remove()⁡
# ⁡⁣⁢⁣it is used to remove element in perticluar value⁡

b = {11,22,33,44}
b.remove(22)
print(b)
# {33, 11, 44}


# ⁡⁢⁣⁣discard()⁡
# ⁡⁣⁢⁣it is used to remove emelent but cannot exist element in list it cannot throw eror⁡

c = {111,222,333,444}
print(c.discard(555))
# None (if not exist)


# ⁡⁢⁣⁣pop()⁡
# ⁡⁣⁢⁣it is used to remove element from first⁡

d = {121,144,167,198}
d.pop()
print(d)
# {121, 198, 167}


# ⁡⁢⁣⁣update()⁡
# ⁡⁣⁢⁣it is used to add multiple element in set

e = {10,20,30,40}
f = {50,60,70}

e.update(f)
print(e)
# {50, 20, 70, 40, 10, 60, 30}


# ⁡⁢⁣⁣copy()⁡
# ⁡⁣⁢⁣it is used to copy the set⁡

g = {12,13,14,15}
h = g.copy()

print(h)
# {12, 13, 14, 15}




# ⁡⁢⁣⁢set operation method⁡ (⁡⁢⁣⁣important⁡)

# ⁡⁢⁣⁣union() or |⁡
# ⁡⁣⁢⁣Returns all elements from both sets (no duplicates).⁡

a = {1,2,3,4}
b = {3,4,5,6,7}

print(a.union(b))
# {1, 2, 3, 4, 5, 6, 7}


# ⁡⁢⁣⁣inretsection()  or  &⁡
# ⁡⁣⁢⁣Returns elements common to both sets.⁡

k = {1,2,3,4}
v = {2,3,4,5,6}

print(k.intersection(v))
# {2, 3, 4}


#⁡⁢⁣⁣ difference or - ⁡
# ⁡⁣⁢⁣Returns elements present in the first set but not in the second.⁡

a = {1,2,3,4}
b = {2,3,4,5}

print(a.difference(b))
# {1}


# ⁡⁢⁣⁣symmetric_difference() or ^⁡
# ⁡⁣⁢⁣Returns elements not common to both sets.⁡

c = {1,2,3,4}
d = {3,4,5,6}

print(c.symmetric_difference(d))
# {1, 2, 5, 6}




#⁡⁢⁣⁢ Subset / Superset Methods()⁡

# ⁡⁢⁣⁣issubset()⁡
# ⁡⁣⁢⁣Checks if all elements of one set are present in another.⁡

a = {1,2,3,4}
b = {1,2,3,4,5,6,7}

print(a.issubset(b))
# True


# ⁡⁢⁣⁣issuperset()⁡
# ⁡⁣⁢⁣Checks if one set contains all elements of another.⁡

c = {1,2,3,4}
d = {1,2}

print(c.issuperset(d))
# True


# ⁡⁢⁣⁣isdisjoint()⁡
# ⁡⁣⁢⁣Checks if two sets have no common elements.⁡

k = {100,200,300}
j = {400,500,600}

print(k.isdisjoint(j))
# True

