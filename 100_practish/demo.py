
a = open('file.txt','w')
a.write('hii, my name is kaushik')
a.close()

a = open('file.txt','w')
a.writelines(['good\n','morning\n'])
a.close()

a = open('file.txt','r')
b = a.readline()
print(b)
a.close()

a = open('file.txt','r')
new = a.readline()
print(new)
a.close()

a = open('file.txt','a')
a.write('we are append in')
a.close()
