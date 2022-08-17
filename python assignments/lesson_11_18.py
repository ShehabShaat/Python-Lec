# created by : shehab shaat 11/8/2022

# ===============================assignment 1======================================
name = "Shehab"
age = 22
country = "Palestine"
print("\"Hello '{:s}".format(name) + "', How You Doing \ \"\"\" Your Age Is \"{:d}".format(
    age) + "\"\"" + " And Your Country Is : {:s}".format(country))
# output
# "Hello 'Shehab', How You Doing \ """ Your Age Is "22"" And Your Country Is : Palestine

# ===============================assignment 2======================================
print("\"Hello '{:s}".format(name) + "', How You Doing \ \n\"\"\" Your Age Is \"{:d}".format(
    age) + "\"\"" + " + \n And Your Country Is : {:s}".format(country))

# ===============================assignment 3======================================
# this assignment i used formatting new & old ways , Escape seq char and concatenation
name = "Elzero"
print("Second Letter Is \"" + name[1] + "\"\nThird Letter Is \"{:s}".format(name[2]) + "\" \nLast Letter Is \"%s" % (
    name[-1]) + "\"")

# ===============================assignment 4======================================
print("\"" + name[1:4] + "\"\n\"{:s}".format(name[::2]) + "\" \n\"%s" % (
    name[-2::-2]) + "\"")

# ===============================assignment 5======================================
name = "#@#@Elzero#@#@"
print(name.strip("#@"))

# ===============================assignment 6======================================

num1, num2, num3, num4, num5 = "9", "15", "130", "950", "1500"
print(num1.zfill(4) + "\n" + num2.zfill(4) + "\n" + num3.zfill(4) + "\n" + num4.zfill(4) + "\n" + num5.zfill(4) + "\n")

# ===============================assignment 7======================================
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# ===============================assignment 8======================================
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())
# ===============================assignment 9======================================
msg = "I Love Python And Although Love El-zero Web School"
print(msg.find("Love", 0, -1))

# ===============================assignment 10 ======================================
name = "Elzero"
print(name.index("z"))

# ===============================assignment 11 ======================================
msg = "I <3 Python And Although <3 El-zero Web School"
print(msg.replace("<3", "Love", 1))
# ===============================assignment 12 ======================================
msg = "I <3 Python And Although <3 El-zero Web School"
print(msg.replace("<3", "Love"))

# ===============================assignment 12 ======================================
name = "Shehab"
age = 22
country = "Palestine"

print("My Name Is {:s}".format(name) + ", And My Age Is {:d} ".format(
    age) + ", And My Country Is {:s}".format(country))
