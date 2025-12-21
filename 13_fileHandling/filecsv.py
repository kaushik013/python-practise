
import csv

f0 = open('emo.csv','w')

f1 = csv.writer(f0)
f1.writerow(['Ename','sql'])
f1.writerows([['kaushik',20000],['jay',3000]]) 
f0.close()


f0 = open('emo.csv','r')
f1 = csv.reader(f0)
print(list(f1))
f0.close()

