# created by : shehab shaat 12/8/2022
# ===============================assignment 1======================================

name = "Shehab",
print(name[0] + "\n" + "{}".format(type(name)))
# ===============================assignment 2======================================
friends = ("Osama", "Ahmed", "Sayed")
a = list(friends)
a[0] = "Elzero"
friends = tuple(a)
print("{}".format(friends) + "\n" + "{}".format(type(friends)) + "\n" + "{}".format(len(friends)))

# ===============================assignment 3======================================
nums = (1, 2, 3)
letters = ("A", "B", "C")
a = nums + letters
print("{}".format(a) + "\n" + "{}".format(len(a)))
# ===============================assignment 4======================================
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print("{}".format(a)+"\n"+"{}".format(b)+"\n"+"{}".format(c))


