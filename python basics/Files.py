# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

import os

# Main Current Working Directory
# print(os.getcwd())
#
# # Directory For The Opened File
# print(os.path.dirname(os.path.abspath(__file__)))
#
# # Change Current Working Directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
#
# print(os.getcwd())
#
# print(os.path.abspath(__file__))
#
# # file = open(r"D:\Python\Files\nfiles\osama.txt")
#
# # file = open("D:\Python\Files\osama.txt")
#
#
# # ===================================Read File========================================
# print("=" * 50)
# myFile = open(r"C:\Users\shehab\Desktop\Python Toturial\python basics\files\shehab.txt", "r")
# print(os.getcwd())
# print(myFile)  # Data object
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)
#
# # print(myFile.read())
# # print(myFile.read(5))  # reade 5 char
# # print(myFile.read())  # complete all lines after char 5
#
# # print(myFile.readlines(5))
# # print(myFile.readlines())
#
#
# for line in myFile:
#     print(line)
#     if line.endswith("5"):
#         break
#
# myFile.close()

# ===================================Write and Append In File=======================================


print(os.chdir(r"/python basics\files"))
print(os.getcwd())

myFile = open("fun.txt", "w")
myFile.write("I Love Python\n" * 1000)

myFile = open("shehab.txt", "w")
myFile.write("I Love ..\n" * 1000)
print(myFile)

myList = ["sheHAb\n", "Ali\n", "ShaAt\n"]
myFile = open("list.txt", "w")
myFile.writelines(myList)

myFile = open("list.txt", "a")
myFile.write("Hello\n")
myFile.write("Third line\n")

# ===================================Important Info=======================================
myFile = open("truncate.txt", "a")
# myFile = open(r"C:\Users\shehab\Desktop\Python Toturial\python basics\files\truncate.txt, "r")

myFile.write("Hello sheHAb\n")
myFile.truncate(5)  # Cut the first 5 letters => Hello

myFile = open("tell.txt", "a")
# myFile = open(r"C:\Users\shehab\Desktop\Python Toturial\python basics\files\tell.txt, "r")

myFile.write("Hello\n")  # \n =>  "2 char"
print(myFile.tell())  # position cursor => 7
#
myFile = open("seek.txt", "r")
# myFile = open(r"C:\Users\shehab\Desktop\Python Toturial\python basics\files\seek.txt, "r")
myFile.seek(6)  # Point the cursor to a specific location
print(myFile.read())
#
os.remove("remove.txt")
# os.remove(r"C:\Users\shehab\Desktop\Python Toturial\python basics\files\remove.txt")
