# import SQLite3
import sqlite3


# Create Database And Connect
db = sqlite3.connect("list.db")

# setting up cursor
cr = db.cursor()
# Create The table and field
cr.execute("CREATE TABLE if not exists family (user_id integer,user_name text)")


my_family = ["shehab", "essam", "diya", "abed", "nour", "yasser", "huda", "ryan", "bashar", "ghassan"]

# insert data
# for name_id, name in enumerate(my_family, 1):
#     cr.execute(f"insert into family (user_id,user_name) VALUES ({name_id},'{name}')")

# delete data
# cr.execute(f"delete from family where user_id={name_id} and user_name='{name}' ")
# or
# cr.execute(f"delete from family )

# update table
# cr.execute("update  family set user_name = 'ShehabEldin' where user_name = 'shehab';")

# drop table
# cr.execute("drop table family")


# fetch data
# cr.execute("select * from family")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

# print(cr.fetchall())

# print(cr.fetchmany(2))

# save all data => commit
db.commit()

# close database => close
# db.close()
#
