
import json
import csv
import pickle

#! writer
with open('data.csv','w',newline='') as wrt:
    obj = csv.writer(wrt)
    obj.writerow(['Name','Age','marks'])
    obj.writerows([['kaushik',22,51],['Janvi',21,34],['Ram',23,98]])

# with open('data.csv','r') as var:
#     data = var.readlines()
#     secured = json.dumps(data)
#     print(secured,type(secured))


# decreptec = json.loads(secured)
# print(decreptec,type(decreptec))

with open('data.csv','r') as var:
    data = var.readlines()

secured = pickle.dumps(data)
print(secured,type(secured))

decreptec = pickle.loads(secured)
print(decreptec,type(decreptec))


