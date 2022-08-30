#  created by : shehab shaat 30/8/2022
# ===============================assignment 1=========
import os

n = 1
os.getcwd()
while n <= 50:
    if n == 25:
        Text50 = open(f"files/special-text.txt", "w")
    else:
        Text50 = open(f"files/txt{n}.txt", "w")
        Text50.write(f"Elzero Web School => {n}\n")
        if n == 1:
            Text50 = open(f"files/txt1.txt", "a")

            Text50.writelines("Appended => Elzero Web School\n" * 50)
        else:
            pass
    n += 1

print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__)[os.path.abspath(__file__).rindex("\\") + 1:])
print(n)
print("=" * 50)
# ===============================assignment 2=========
Text50 = open(f"files/txt1.txt", "r")

print(Text50.read())
print("=" * 50)
# ===============================assignment 3=========
num_line = 0
myList = []
count = 0
for line in open(f"files/txt1.txt", "r"):
    myList += list(line.split())
    count += line.count("l")
    num_line += 1

print(f"Number Of Lines Is => {num_line}")
print(f"Number Of Words Is => {len(myList)}")
print(f"Number Of Chars Is => {Text50.tell() - num_line - len(myList)}")
print(f"Number Of l Is => {count}")

# ===============================assignment 4=========

r = 41
while r <= 50:
    os.remove(fr"C:\Users\shehab\Desktop\Python Toturial\python assignments\files\txt{r}.txt")
    r += 1
