

# ⁡⁣⁣⁢Create a new file "practice.txt" using python. Add the following data in it:

# ⁡⁢⁣⁣Hi everyone
# we are learning File 1/0
# using Java.
# I like programming in Java.⁡


with open('practice.txt','w')as fs:
    fs.write('Hi everyone \nwe are learning File 1/0 \nusing Java. \nI like programming in Java')
    print('file created successfully! ')



# ⁡⁢⁣⁣WAF that replacesall occurrences of Java" with "python" in above file.⁡

with open('practice.txt','r')as fs:
    data = fs.read()
new_data = data.replace('Java','Pyhton')
print(new_data)

with open('practice.txt','w')as fs:
    fs.write(new_data)



# ⁡⁢⁣⁣Search if the word learning" exists in the file or not.⁡

world = 'learning'
with open('practice.txt','r')as fs:
    data = fs.read()
    if(data.find(world) != -1):
        print('found')
    else:
        print('not found')


def check_line():
    word = 'learning'
    data = True
    line_no = 1
    with open('practice.txt','r')as fs:
        while data:
            data = fs.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1


# ⁡⁣⁣⁢binary file handling⁡

from PIL import Image
import io

with open('13_fileHandling/sketch1730955868079 copy.png','rb')as fs:
    data = fs.read()

img = Image.open(io.BytesIO(data))
img.show()