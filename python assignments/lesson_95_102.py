# created by : shehab shaat 29/9/2022

# ===============================assignment 1======================================
# regular expression =================> (\w\b) <=======================
# https://regex101.com/r/iXVVZO/1

import re

string1 = re.findall(r"(\w\b)", "eeeeE llllLl lllzzZzzzz eroe operationr pollo")
for _ in string1:
    print(_, end="")
print("\n" + "=" * 50)
# ===============================assignment 2======================================
# regular expression =================> (\bL\w+) <=======================
# https://regex101.com/r/KC8Iuf/1

string2 = re.findall(r"(\bL\w+)", "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111")
for _ in string2:
    print(_)
print("=" * 50)
# ===============================assignment 3======================================
# regular expression =================> ^(\W?\(\d+\)\s\d+-?\d{4})$ <=======================
# https://regex101.com/r/30694Z/1

import os

phone_number = open(r"files\phone_number.txt", "r")
string3 = re.findall(r"^(\W?\(\d+\)\s\d+-?\d{4})$", phone_number.read(), re.M)
for _ in string3:
    print(_)

print("=" * 50)
# ===============================assignment 4======================================
# regular expression =================> ^(https?://(\w+.)?\w+.(com|org)(:8888)?/\w+.\w+)$<=======================
# https://regex101.com/r/AOp61j/1

website = open(r"files\website.txt", "r")
string4 = re.findall(r"^(https?://(\w+.)?\w+.(com|org)(:8888)?/\w+.\w+)$", website.read(), re.M)
for _ in string4:
    print(_)
# ===============================assignment 5======================================
print("=" * 50)
# regular expression :
# 1) https?
# 2) https|http
# 3) [^a-d]+
# 4) http\w?
# 5) https*

string5 = re.findall(r"https|http", "http\nhttps\nabcd\nabcd")
for _ in string5:
    print(_)