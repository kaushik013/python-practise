

#⁡⁣⁣⁢ sum of value ⁡

a = {1:11,2:12,3:13,4:14,5:15}
b = {5:15,6:16,7:17,8:18,9:19}

for i in b:
    a[i] = b[i]
print(a)

sum = 0
for i in a.values():
    sum = sum + i
print(sum)

# 135


# ⁡⁣⁣⁢⁡⁣⁣⁢marge two number⁡

a = {1:11,2:12,3:13,4:14,5:15}
b = {5:15,6:16,7:17,8:18,9:19}

for i in b:
    a[i] = b[i]
print(a)


a = [1,1,1,2,2,2,3,3,3,3,4,4,5,6,7,7,7,8,8,9]

dist = {}

for i in a:
    if(i in dist.keys()):
        dist[i] += 1
    else:
        dist[i] = 1
print(dist)


# ⁡⁣⁣⁢how to add in dict and if duplicate value then += in keys⁡

d1 = {1:100,2:200}
d2 = {2:300,3:300}

emp = {}

for k,v in d1.items():
    emp[k] = v

for k,v in d2.items():
    if(k in emp):
        emp[k] += v
    else:
        emp[k] = v

print(emp)
