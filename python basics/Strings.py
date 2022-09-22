singleQuote = 'hello Python "test "'
doubleQuote = "hello Python 'test' "
print(singleQuote)
print(doubleQuote)

# multiple line triple double Quote ,
# this case will make ignore to the new line ,so will be like this :
# [multiple "first"  'test' line ]

multipleLine1 = """hello
multiple "first"  'test' \
line """
print(multipleLine1)

# multiple line triple single Quote
# this case don't make ignore to the new line but will be ignore one slash only ,so will be like this :
# [multiple "first" \ 'test'  ]

multipleLine2 = '''hello
multiple "first" \\ 'test'
line '''
print(multipleLine2)

# ================================Indexing And Slicing================================
# Indexing [Accesses single item]
print("===========================================")
my_str = 'I love Palestine'
print(my_str[0])  # index[0] => I
print(my_str[5])  # index[5] => e
print(my_str[-1])  # index[-1] => -1 first character fom end
print("===========================================")
# Slicing [Accesses multiple sequence item]
# [Start : End ] End not Encoded
# [Start : End : step] End not Encoded

print(my_str[0:1])
print(my_str[2:6])
print(my_str[7:16])
print(my_str[:7])  # if start is not exist well be start index 0
print(my_str[0:])  # if end is not exist well be going to last index
print(my_str[:])  # full data
print(my_str[::1])  # full data
print(my_str[0::1])  # full data
print(my_str[0::2])  # full data

# ================================ Strings Methods ================================
print(len(my_str))  # number of char in string

# 1)  strip() rstrip() lsrtip() [to remove spacing right , left ,both in the string]
my_str2 = ' I love Palestine '
print(my_str2.strip())
print(my_str2.rstrip())  # remove only spacing to the right side
print(my_str2.lstrip())  # remove  only spacing to the left side
my_str3 = '####I love Palestine####'
print(my_str3.strip("#"))
print(my_str3.rstrip("#"))
print(my_str3.lstrip("#"))
my_str3 = '$#$#$#$#I love Palestine$#$#$#$#'
print(my_str3.strip("$#"))
print(my_str3.rstrip("$#"))
print(my_str3.lstrip("$#"))

# 2) title()
# convert first char from every word and any char after number
my_str4 = "i love 2d palestine 3d "
print(my_str4.title())
# 3) capitalize
# convert first char for the line
print(my_str4.capitalize())

# 4) z fill [zero fill]
a, b, c = "1", "11", "111"
print(c.zfill(3))
print(a.zfill(3))
print(b.zfill(3))

print("================================")
# 5) upper, lower
name = "shehab shaat"
print(name.upper())
print(name.lower())

# 6) center()
e = "shehab"
print(e.center(8))
print(e.center(8, "#"))

# 7) count()
print(my_str2.count("love"))
print(my_str2.count("love", 0, 15))

# 8 ) Split
a = "I-love-Python-and-Php"
s = "I love Python and Php"
print(a.split("-"))
print(s.split())

# 9 ) swapcase
g = "I love Python"
f = "I love pYTHON"
print(g.swapcase())
print(f.swapcase())

# 10 ) startswith & endswith
print(g.startswith("I"))
print(g.startswith("P", 7, 12))
print(g.endswith("n"))
print(g.endswith("e", 2, 6))

# 11) Index & find
print(g.index("P"))
print(g.index("P", 0, 10))
# print(g.index("P", 0, 5)) error

print(g.find("P"))
print(g.find("P", 0, 10))
print(g.find("P", 0, 5))  # -1

# 12) rjust(Width,Fill Char) [right justified : Put the original text on the right ]
# [width:number of character to be added]
# fill char : character to be added
# ijust(Width,Fill Char)  [left justified : Put the original text on the left ]
c = "Shehab"
print(c.rjust(10, "#"))
print(c.ljust(10, "#"))

# 13) splitline()
c = """first line
second line
third line """
# print(type(c.splitlines()))
print(c.splitlines())
c = "first line\nsecond line\nthird line "
print(c.splitlines())

# 14) expandtabs()
c = "first line\tsecond line\tthird line "
print(c.expandtabs(21))

# 15) istitle()
one = "I love Python , 3g and Kotlin"
print(one.istitle())
one = "I love Python , 3g and Kotlin"
print(one.title())
# 16) isspace()
one = " "
print(one.isspace())

# 17) islower()
one = "shehab"
print(one.islower())

# 18) isidentifier()
one = "shehab--"
tow = "shehabShaat"
three = "s_sh"
print(one.isidentifier())
print(tow.isidentifier())
print(three.isidentifier())

# 19) isalpha()
x = "AaaaabbbBcccC"
print(x.isalpha())
x = "Aa5aaabbbBcccC"
print(x.isalpha())

# 20) isalnum()
x = "AaaaabbbBcccC"
print(x.isalnum())
x = "Aa5aaabbbBcccC"
print(x.isalnum())

# 21) replace() (old value,new value,count)
replace = "hello one one three tow"
print(replace.replace("one", "1"))
print(replace.replace("one", "1", 1))

# 22) join(Iterable)
mylist = ["Shehab", "Essam", "shaat"]
print("-".join(mylist))
print(" ".join(mylist))
print(type("-".join(mylist)))
# 23) removeprefix & removesuffix  (new method python 3.9)
name = "Hello world"
print(name.removeprefix("Hel"))
print(name.removesuffix("ld"))

# 24) String Repeat (*)
myString = "shehab"
print(myString * 6)
