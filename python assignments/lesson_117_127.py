# created by : shehab shaat 30/9/2022

# import SQLite3
import sqlite3

# ========================================assignment 1=============================================================
# integers, characters, strings, floating-point numbers and arrays.


# ========================================assignment 2=============================================================

# Create Database And Connect
db = sqlite3.connect(r"Python\elzero.db")

# setting up cursor
cr = db.cursor()
# Create The table and field
cr.execute("CREATE TABLE if not exists users (user_id integer unique ,user_name text unique ,date text  ,email text  "
           "unique )")
# ========================================assignment 3=============================================================
# insert data

# cr.execute(f"insert into users (user_id,user_name,date,email) VALUES (1,'shehab','5/8/2000','shaatshehab@gmail.com')")
# cr.execute(f"insert into users (user_id,user_name,date,email) VALUES (2,'abed','7/8/1998','abed@gmail.coom')")
# cr.execute(f"insert into users (user_id,user_name,date,email) VALUES (3,'nour','28/11/2001','nour@gmail.coom')")
# cr.execute(f"insert into users (user_id,user_name,date,email) VALUES (4,'bashar','5/5/2005','bashar@gmail.coom')")
# cr.execute(f"insert into users (user_id,user_name,date,email) VALUES (5,'diya','5/3/2007','diya@gmail.coom')")
#


# ========================================assignment 4=============================================================

cr.execute("select * from users where user_id=5")
print(cr.fetchone())
# ========================================assignment 5=============================================================
user_id = int(input("Enter the number of the member you want to delete : "))
mylist = []
cr.execute("select * from users ")
result = cr.fetchall()
for _ in range(len(result)):
    mylist.append(result[_][0])

if user_id in mylist:
    cr.execute(f"delete from main.users where user_id={user_id}")
    print("User Deleted.")
    cr.execute("select * from users ")
    result = cr.fetchall()
    for _ in range(len(result)):
        print(f"ID => {result[_][0]}, Name => {result[_][1]}, Date Of Birth => {result[_][2]}, Email => {result[_][3]}")
else:
    print("User Not Found.")

# save all data => commit
db.commit()

# close database => close
db.close()
