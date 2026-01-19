

# 1. From string `"Python"`, create a dictionary where key = character, value = ASCII value

# 2. Given `nums = [10, -5, 8, -3, 0, 12]`, create a dictionary with key = number, value = `"Positive"` **only for positive numbers**.

# 3. Get the following output
# a=`["Apple", "Banana", "Cherry", "Dates","Orange","Ice apple"]
# output={'Apple':"A","Banana":"b","Cherry":"c","Dates":"d","Orange":"O","Ice apple":"I"}`

# 4. Get the following output
# a=["Ananya", "Rohit", "Sneha", "Aarav", "Meera”]
# b=[85, 72, 90, 67, 88]
# find average marks, then create a dictionary `{name: "Above Avg" or "Below Avg"}`.

# 5. From the string `"programming"`, count occurrences of each character using dictionary comprehension.

# 6. Get the following output
# s= "python is fun and python is easy”
# output={'python':2, 'is':2, 'fun':1, 'and':1, 'easy':1}




#! 1. From string `"Python"`, create a dictionary where key = character, value = ASCII value
str='Python'
dic = {}

for i in str:
    dic[i]=ord(i)
# print(dic) 

result={i:ord(i) for i in str}
# print(result)



#! 2. Given `nums = [10, -5, 8, -3, 0, 12]`, create a dictionary with key = number, value = `"Positive"` **only for positive numbers**.
nums = [10, -5, 8, -3, 0, 12]
dic = {}
for i in nums:
    if i>=0:
        dic[i]='Positive'
# print(dic)

result={i:'Positive' for i in nums if i>=0}
# print(result)



#! 3. Get the following output
# a=`["Apple", "Banana", "Cherry", "Dates","Orange","Ice apple"]
# output={'Apple':"A","Banana":"b","Cherry":"c","Dates":"d","Orange":"O","Ice apple":"I"}`

a = ["Apple", "Banana", "Cherry", "Dates","Orange","Ice apple"]
dic = {}
for i in a:
    if len(i)%2!=0:
        dic[i]=i[0].upper()
    else:
        dic[i]=i[0].lower()
# print(dic)

result={ i:i[0].upper() if len(i)%2!=0 else i[0].lower() for i in a}
# print(result)




# ! 4. Get the following output
# a=["Ananya", "Rohit", "Sneha", "Aarav", "Meera”]
# b=[85, 72, 90, 67, 88]


# find average marks, then create a dictionary {name: "Above Avg" or "Below Avg"}

a=["Ananya", "Rohit", "Sneha", "Aarav", "Meera"]
b=[85, 72, 90, 67, 88]

avg = sum(b)/len(b)
print(avg)

dic = {}
for i,j in zip(a,b):
    if j >= avg:
        dic[i] = "Above Avg"
    else:
        dic[i] = "Below Avg"
# print(dic)

result={ i:'Above Avg' if j >= avg else 'Below Avg' for i,j in zip(a,b)}
# print(result)


# !5. From the string `"programming"`, count occurrences of each character using dictionary comprehension.

str='Programming'
out={}
for i in str:
    out[i]=str.count(i)
# print(out)

result={ i:str.count(i) for i in str }
# print(result)



#! 6. Get the following output
# s= "python is fun and python is easy”
# output={'python':2, 'is':2, 'fun':1, 'and':1, 'easy':1}

s= "python is fun and python is easy"
sp=s.split()
out={}

for i in sp:
    out[i]=sp.count(i)
# print(out)

result={ i:sp.count(i) for i in sp}
# print(result)