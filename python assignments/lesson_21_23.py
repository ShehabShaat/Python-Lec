# created by : shehab shaat 12/8/2022

# ===============================assignment 1======================================
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
x, _, _, _, _ = friends
_, _, _, _, y = friends

print(friends[0])
print(x)
# print(friends[0:1])
print(friends[-1])
print(y)
# print(friends[-1:])
# ===============================assignment 2======================================
print(friends[0::2])
print(friends[1::2])
# ===============================assignment 3======================================
print(friends[1:-1])
print(friends[-2:])
# ===============================assignment 4======================================
friends[-2:] = ["Elzero", "Elzero"]
print(friends)
# ===============================assignment 5======================================
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
print(friends)
friends.append("Salem")
print(friends)
# ===============================assignment 6======================================
friends.remove(str(friends[0]))
friends.remove(str(friends[0]))
print(friends)
friends.remove(str(friends[-1]))
print(friends)
# ===============================assignment 7======================================
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)
# ===============================assignment 8======================================

friends.sort()
print(friends)
friends.sort(reverse = True)
print(friends)

# ===============================assignment 9======================================
print(len(friends))
# ===============================assignment 10======================================
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])
