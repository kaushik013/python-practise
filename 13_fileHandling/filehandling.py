

# ⁡⁢⁣⁣what is file handling⁡

# ⁡⁣⁣⁢File handling means reading from and writing to files stored on your computer (like .txt, .csv, etc.) 
# using Python code.⁡


# ⁡⁢⁣⁣File Modes:⁡

# ⁡⁢⁣⁢Mode	Meaning	Example⁡

# ⁡⁣⁢⁣'r'	        Read (default mode)	file must exist
# 'w'	        Write (creates or overwrites file)	file = open("data.txt", "w")
# 'a'	        Append (adds data at the end)	file = open("data.txt", "a")
# 'r+'	        Read and write	file = open("data.txt", "r+")
# 'w+'	        Write and read	file = open("data.txt", "w+")⁡



# 🔹 Summary Table

# ⁡⁢⁣⁣Function	  ⁡             ⁣Description⁡
# ⁡⁢⁣⁣file.read()⁡	            ⁡⁣⁢⁣Reads entire content⁡
# ⁡⁢⁣⁣file.readline() ⁡  	    ⁡⁣⁢⁣Reads one line⁡
# ⁡⁢⁣⁣file.readlines()⁡  	    ⁡⁣⁢⁣Reads all lines into a list⁡  
# ⁡⁢⁣⁣file.write("text")⁡	    ⁡⁣⁢⁣Writes to file⁡
# ⁡⁢⁣⁣file.close()⁡	        ⁡⁣⁢    ⁣Closes the file⁡
# ⁡⁢⁣⁣with open()⁡	        ⁡⁣⁢    ⁣Automatically closes file⁡



# ⁡⁢⁣⁣mode to open file⁡

# ⁡⁣⁢⁣'r' ---> read mode (file must exist) 📖
# 'w' ---> write - create a file or overwrite 📝
# 'a' ----> appdend - adds to end of file 🧑🏻‍⚖️
# 'x' ----> create - creates a new file fails if it exist ⁡䷀
# ⁡⁣⁢⁣'b' ----> binary mode
# 't' ----> text mode
# '+' ----> open a disk file for updating(read and write)⁡
# ⁡⁣⁢⁣'r+'⁡ ⁡⁣⁢⁣----> open read and writion mode ⁡⁢⁣⁣{no truncate  secured!}⁡ ✅
# ⁡⁣⁢⁣ w+ ----> read + override pointer start⁡ ⁡⁢⁣⁢{ truncate }⁡ ❌
# ⁡⁣⁢⁣a+ ----> read + append pointer end⁡ ⁡⁢⁣⁣{no truncate}⁡ ✅


# # ⁡⁢⁣⁣create file ⁡
# name = input('enter file name : ')
# text = input('enter text : ')


# with open(name,'w')as fs:
#     fs.write(text)
#     print(f'{name} file created! ✅')

# # ⁡⁢⁣⁣read data⁡
# with open(name,'r')as fs:
#     data = fs.read()
#     print(data)


# # ⁡⁢⁣⁣append text⁡
# with open(name,'a')as fs:
#     new_data = input('enter text to added ! : ')
#     fs.write('  '+ new_data)

# with open(name,'r')as fs:
#     data = fs.read()
#     print(data)



# #  ⁡⁢⁣⁣for delete file ⁡
# import os
# os.remove(name)

