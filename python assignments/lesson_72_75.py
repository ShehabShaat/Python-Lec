#  created by : shehab shaat 6/9/2022
# ===============================assignment 1======================================
from functools import reduce


def remove_chars(string):
    return str(string)[1:-1]


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars, friends_map)
for _ in cleaned_list:
    print(_)
print("#" * 50)
# cleaned_list = map(lambda string: str(string)[1:-1], friends_map)
# for _ in cleaned_list:
#     print(_)
for _ in map(lambda string: str(string)[1:-1], friends_map):
    print(_)


# ===============================assignment 2======================================

def get_names(text):
    if text[-1] == "m":
        return text


print("=" * 50)

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
cleaned_list = filter(get_names, friends_filter)
for _ in cleaned_list:
    print(_)

# ===============================assignment 3======================================
print("=" * 50)


def productAll(num1, num2):
    return num1 * num2


nums = [2, 4, 6, 2]

res = reduce(productAll, nums)
print(res)

res = reduce(lambda num1, num2: num1 * num2, nums)

print(res)

# ===============================assignment 4======================================
print("=" * 50)

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

mySkillsWithCounter = enumerate(reversed(skills), 50)

for counter, skill in mySkillsWithCounter:
    if str(skill).isdigit():
        continue
    else:
        print(f"{counter} - {skill}")

print("#" * 50)
count = 50
for n in reversed(skills):
    if str(n).isdigit():
        count += 1
        continue
    else:
        print(f"{count} - {n}")
        count += 1
