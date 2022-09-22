# ----------------------------------
# -- Regular Expressions => Intro --
# ----------------------------------
# [1] Sequence of Characters That Define A Search Pattern
# [2] Regular Expression is Not In Python Its General Concept
# [3] Used In [Credit Card Validation, IP Address Validation, Email Validation]
# [4] Test RegEx "https://pythex.org/"
# [5] Characters Sheet "https://www.debuggex.com/cheatsheet/regex/python"
# ----------------------------------------
# -- Regular Expressions => Quantifiers --
# ----------------------------------------
# *	0 or more
# +	1 or more
# ?	0 or 1
# {2}	Exactly 2
# {2, 5}	Between 2 and 5
# {2,}	2 or more
# (,5}	Up to 5
# +972 597747241=> https://regex101.com/r/GHtySL/1
# -----------------------------------------------------------------------
# -- Regular Expressions => Characters Classes Training's --
# -----------------------------------------------------------------------
# [0-9] : Number From 0 to 9
# [^0-9] : Anything Except 0-9
# [A-Z] : Characters Form A to Z
# [^A-Z] : Anything Except Characters From A  to Z
# [a-z]
# [^a-z]
# [A-z] : All Characters
# shabbinessSaat
# 0597747241
#  https://regex101.com/r/OcwAmK/1
# ---------------------------------------
# -- Regular Expressions => Assertions --
# ---------------------------------------
# ^	  Start of String
# $	  End of string
# -------------------------
# Match Email
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$
# https://regex101.com/r/PoWbVs/1
# ----------------------------------------------------
# -- Regular Expressions => Logical Or And Escaping --
# ----------------------------------------------------
# |	  Or
# \	  Escape Special Characters
# ()  Separate Groups
# https://regex101.com/r/Z665jF/1
# https://regex101.com/r/0pJYBA/1
# -----------------------------

# (\d-|\d\)|\d>) (\w+)
# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\))
# ^(https?://)(www\.)?(\w+)\.(net|org|com|info|me)$
# https://regex101.com/r/RI0h5C/1


# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------
import re

my_email1 = re.search("[A-Z]", "SheHab")
my_email2 = re.search(r"[A-Z]{2}", "SHaAt")

print(my_email1)
print(my_email2)

print(my_email1.span())  # span=(0, 1) => position
print(my_email2.span())  # span=(3, 4) => position

print(my_email1.string)
print(my_email2.string)

print(my_email1.group())
print(my_email2.group())

# your_email = input("Enter your Email: ")
# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.[A-z]+", your_email)
# if is_email:
#     print("valid email")
#     print(is_email.group())
# else:
#     print("invalid email")


your_email = input("Enter your Email: ")
is_email = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.[A-z]+", your_email)
my_List = []
if is_email != []:
    my_List.append(is_email)
    print("valid email and add")

else:
    print("invalid email")

for email in my_List:
    print(email)

# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ---------------------------------------------------------------------
string = "I Love Python"
my_search = re.split(r"\s", string)
print(my_search)

string = "I Love Python"
my_search = re.split(r"\s", string, 1)
print(my_search)

string = "I-Love-Python_And_Django"
my_search = re.split(r"-|_", string)
print(my_search)

for _ in enumerate(my_search):  # counter
    print(_)

for counter, _ in enumerate(my_search):  # counter
    if len(_) == 2 or len(_) == 1:
        continue
    else:
        print(f"{counter}- {_}")

print(re.sub("\s", "-", "I Love Python"))
print(re.sub("\s", "-", "I Love Python", 1))

# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------

import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"
# (https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+) ==> reg Exp url
search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web, re.M)  # re.M = > multiline
print(search.group())
print(search.groups())
for counter, _ in enumerate(search.groups()):
    print(f"{counter}- {_}")

print(search.group(1))
