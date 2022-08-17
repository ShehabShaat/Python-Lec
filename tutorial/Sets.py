# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

mySetOne = {"Shehab", "essam", "shaat"}

# not ordered and not indexed

print(mySetOne)

# Indexing and Slicing Can't be Done
mySetTow = {1, 2, 3, 4}
# print(mySetOne[0]) error

# Has Only Immutable Data Types
# mySetThree = {"Shehab", 3, 4, True, [1, 2, 5]}
# print(mySetThree)  # TypeError: unhashable type: 'list'
# hashing : mechanism in computer science allow to search quickly for object in memory
mySetFour = {"Shehab", 3, 4, True, (1, 2, 5)}
print(mySetFour)
print("=" * 40)
# Items Is Unique
mySetFive = {1, 2, "Shehab", "One", "Shehab", 3}
print(mySetFive)

"====================================Set Method==============================="
# Clear()
print("=" * 40)
a = {1, 2, 3}
a.clear()
print(a)
print("=" * 40)
# Union()
b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
# e = ["4", "5"]
f = {"4", "5"}
print(b | c)
print(b.union(c))
print(b.union(c, f))
print("=" * 40)
# add()
d = {1, 2, 3, 4}
print("=" * 40)
# d.add(5, 6) error , one argument only
d.add(5)
print(d)
print("=" * 40)
# copy()
j = {1, 2, 3, 4}
l = j.copy()
print("=" * 40)
print(j)
print(l)
j.add(5)
print(j)
print(l)
print("=" * 40)
# remove()
r = {1, 2, 3, 6}
# r.remove(5) error because num 5 is not found
r.remove(1)
print(r)
print("=" * 40)
# discard() don't action error when element in arg is not found
k = {1, 2, 3, 7}
k.discard(5)
print(k)
print("=" * 40)
# pop()
i = {"A", True, 1, 2, 3}
print(i.pop())
print(i)
print("=" * 40)
# update()
s = {1, 2, 3}
q = {1, "A", 6, "B"}
s.update(q)
print(s)
s.update([12, 6, 8])
print(s)
print("=" * 40)
#  difference()
a = {1, 2, 3, 4}
b = {1, 2, 3, "Shehab", "shaat"}
print(a.difference(b))  # a-b print difference only
print(a)
print("=" * 40)
# difference_update()
a = {1, 2, 3, 4}
b = {1, 2, "Shehab", "shaat"}
print(a)
a.difference_update(b)  # update original sit
print(a)
print("=" * 40)

a = {1, 2, 3, 4, "X"}
b = {"Shehab", "X", 2}
print(a)
print(a.intersection(b))
print(a)

a = {1, 2, 3, 4, "X", "Shehab"}
b = {"Shehab", "X", 2}
print(a)
a.intersection_update(b)
print(a)
print("=" * 40)
# symmetric_difference
a = {1, 2, 3, 4, 5, "X"}
b = {"Shehab", "Zero", 1, 2, "X"}
print(a)
print(a.symmetric_difference(b))  # i ^ j (anything not exist in two set)
print(a)

a = {1, 2, 3, 4, 5, "X"}
b = {"Shehab", "Zero", 1, 2, "X"}
print(a)
a.symmetric_difference_update(b)  # i ^ j (print anything not exist in two set)
print(a)
print("=" * 40)
# issuperset
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
print(a.issuperset(b))
print(b.issuperset(a))
print("=" * 40)
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
print(a.issubset(b))
print(b.issubset(a))
print("=" * 40)
# isdisjoint
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
i = {6, 7, 8}
print(a.isdisjoint(b))
print(a.isdisjoint(i))
