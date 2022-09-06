from functools import reduce

print("all()".center(70, "="))

x = [1, 2, 3, 4, []]
if all(x):  # iterable => list , Tuple , set , Dict
    print("All Element Is True ")
else:
    print("Theres At Least One Element Is False ")
print("any()".center(70, "="))
# ====================================================================
if any(x):  # iterable => list , Tuple , set , Dict
    print("Theres At Least One Element Is True ")
else:
    print("Theres No Any True Element ")
# ====================================================================

print("bin()".center(70, "="))
print(bin(20))
# ====================================================================

print("id()".center(70, "="))
a = 1
b = 2
print(id(a))
print(id(b))
# ====================================================================
print("sum()".center(70, "="))
a = [1, 10, 19, 30]
print(sum(a))
a = [1, 10, 19, 30]
print(sum(a, 40))
# ====================================================================

print("round()".center(70, "="))
print(round(15.5))
print(round(15.4))
print(round(155.555, 2))
# ====================================================================

print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))
# ====================================================================

# print()
print("print()".center(70, "="))

print("Hello @ Shehab @ How @ Are @ You")
print("Hello", "Shehab", "How", "Are", "You", sep=" | ")

print("First Line", end=" ")
print("Second Line")
print("Third Line")

# ====================================================================
# map
print("map()".center(70, "="))


# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function

def formatText(text):
    return f"- {text.strip().capitalize()} -"


myTexts = [" OSama ", "AHMED", "  sAYed  "]

myFormatedData = map(formatText, myTexts)

print(myFormatedData)

for name in list(map(formatText, myTexts)):
    print(name)

print("#" * 50)


# Use Map With Lambda Function

def formatText(text):
    return f"- {text.strip().capitalize()} -"


myTexts = [" OSama ", "AHMED", "  sAYed  "]

for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):
    print(name)

# ====================================================================
# Filter
print("Filter()".center(70, "="))


# Example 1
def checkNum(num):
    return num > 10


myNumber = [0, 0, 1, 5, 6, 9, 75, 61, 0, 8]
result = filter(checkNum, myNumber)  # Return True only

for re in result:
    print(re)

#
print("#" * 50)


# Example 2

def checkName(name):
    return name.startswith("O")


myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myReturnedData = filter(checkName, myTexts)

for person in myReturnedData:
    print(person)

print("#" * 50)

# Example 3

myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

for p in filter(lambda name: name.startswith("A"), myNames):
    print(p)

# ====================================================================
# reduce
print("reduce()".center(70, "="))


def sumAll(num1, num2):
    return num1 + num2


numbers = [1, 8, 2, 9, 100]

result1 = reduce(sumAll, numbers)

result2 = reduce((lambda num1, num2: num1 + num2), numbers)

print(result1)

# ((((1 + 8) + 2) + 9) + 100)


# # ====================================================================
# enumerate(iterable, start=0)
print("enumerate()".center(70, "="))

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 20)

print(type(mySkillsWithCounter))

for counter, skill in mySkillsWithCounter:
    print(f"{counter} - {skill}")

# # ====================================================================
# help()
print("help()".center(70, "="))
print(help(print))

# # ====================================================================
# reversed(iterable)
print("reversed()".center(70, "="))

myString = "Elzero"

print(reversed(myString))

for letter in reversed(myString):
    print(letter)

for s in reversed(mySkills):
    print(s)
