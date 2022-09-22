# references (Strings Formatting) (https://github.com/ShehabShaat/Python/blob/master/README.md)  => ctrl+B
# {} means place holder , : means column
# ============================Formatting old Ways================================
from datetime import datetime

name = "shehab"
age = 22
rank = 10
print("My name is : %s" + name)
print("My name is : %s and my age is : %d" % (name, age))
print("my name is : %s and my age is : %d and my rank is : %f" % (name, age, rank))
# %s => String
# %f => flout
# %d => Number

n = "shehab"
l = "Python"
y = 3
print("My Name is %s Iam %s Developer with %d years Exp" % (n, l, y))

# control floating point number
myNumber = 10
print("My number is : %d" % myNumber)
print("My number is : %f" % myNumber)
print("My number is : %.2f" % myNumber)
# Truncate String
myLongString = "Hello Peoples ,Im shehab shaat ,i love all"
print("Message is %.30s " % myLongString)

# ============================Formatting New Ways================================
name = "shehab"
age = 22
rank = 10
print("My name is : {}".format(name))
print("My name is : {} and my age is : {} ".format(name, age))
print("my name is : {:s} and my age is : {:d} and my rank is :{:f}".format(name, age, rank))
# {:s} => String
# {:f} => flout
# {:d} => Number

n = "shehab"
l = "Python"
y = 3
print("My Name is {:s} Iam {:s} Developer with {:d} years Exp".format(n, l, y))

# control floating point number
yNumber = 10
print("My number is : {:d} ".format(myNumber))
print("My number is : {:f}".format(myNumber))
print("My number is : {:.2f}".format(myNumber))  # old way : %.2f

# Truncate String
myLongString = "Hello Peoples ,Im shehab shaat ,i love all"
print("Message is {:.30s} ".format(myLongString))

# format money
myMoney = 50016235816
print("my money in Bank Is : {:,}".format(myMoney))
print("my money in Bank Is : {:,d}".format(myMoney))
print("my money in Bank Is : {:,f}".format(myMoney))

# Rearrange items

a, b, c = "one", "two", "three"
print("hello {} {} {}".format(a, b, c))
print("hello {2} {1} {0}".format(a, b, c))
print("hello {2} {0} {1}".format(a, b, c))

a, b, c = 10, 20, 30
print("hello {} {} {}".format(a, b, c))
print("hello {2:d} {1:.2f} {0:d}".format(a, b, c))
print("hello {2:f} {0:d} {1:0.1f}".format(a, b, c))

# format in Version
print(f"my name is {n} and may age is {age}")
#  format Datetime
print('{:%Y-%m-%d %H:%M:%S}'.format(datetime(2001, 2, 3, 4, 5,3)))