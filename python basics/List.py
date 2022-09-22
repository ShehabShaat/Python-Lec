# lists are mutable , delete , add, edit
# list Item is not Unique
# list Can Have different Data Types
myList = ["One", "Two", "one", 1, 100.5, True]
#  slice and index
print(myList)
print(myList[1])
print(myList[-1])
print(myList[-3])
print(type(myList[2]))

print(myList[1:4:1])
print(myList[-2:2:-1])  # 100.5, 1
print(myList[-2:2:-2])  # 100.5, 1
print(type(myList[2::2]))

myList[1] = 2
myList[0] = 1 + 5j
# myList[0:3] = []  # Dump the specified values
print(myList)
myList[0:3] = ['a', 'b', 'c']  # Toggle selected values
print(myList)

myList[0:3] = ['a', 'b']  # Toggle selected values
print(myList)
"===============================List Methods==============================="
# 1) append()
myFriends = ["mohammed", "anas", "Ahmed"]
myOldFriends = ["khaled", "Ali", "Ahmed"]
myFriends.append("sage")  # add new element after the last list
myFriends.append(100)
myFriends.append(150.0)
myFriends.append(True)
myFriends.append(myOldFriends)
# added as a one element into list friends
print(myFriends)
# ['mohammed', 'anas', 'Ahmed', 'sage', 100, 150.0, True, ['khaled', 'mahmmod', 'Ahmed']]

print(myFriends[2])
print(myFriends[6])
print(myFriends[7][0])
print(myFriends[7][2])

# 2) extend()

a = [1, 2, 3]
b = ["a", "b", "c"]
a.extend(b)  # add element from list b to list  a , as a one list
print(a)
# [1, 2, 3, 'a', 'b', 'c']
c = ["one", "Two"]
a.extend(c)
print(a)

# 3) remove() (remove first element from "Shehab"
x = [1, 2, 3, 4, 5, True, "Shehab", "hello"]
x.remove(x[6])
print(x)

# 4) sort() & reverse()
y = [1, 2, 100, 120, -10, 17, 29]
y.sort()
print(y)
y.sort(reverse=True)
print(y)
y = ["z", "c", "b", "e", "d", "g", "f"]
y.sort()
print(y)
y.sort(reverse=True)
print(y)
f = ["z", "c", "b", "e", "d", "g", 10]
# f.sort()  # error
# print(f)
f.reverse()
print(f)

# 5) clear()
a = [1, 1, 3, 4]
a.clear()
print(a)
# 6) copy()
b = [1, 2, 3]
c = b.copy()  # shallow copy of the list.
print(b)  # Main list
print(c)  # copied List

b.append("5")

print(b)  # main list ""
print(c)  # copied List

# 7) count()
d = [1, 2, 3, 4, 5, 5, 6, 9, 7, 8]
print(d.count(5))

# 8) Index
print(d.index(5))

# 9) insert() Insert object before index
d = [1, 2, 3, 4, 5, 5, 6, 9, 7, 8]
d.insert(1, "Test")
print(d)
# [1, 'Test', 2 ,3, 5, 4, 5, 5, 6, 9, 7, 8]
d.insert(-1, 'Test')
print(d)
# [1, 'Test', 2, 3, 4, 5, 5, 6, 9, 7, 'Test', 8]


# 10) pop
g = [1, 2, 3,4, 5, 6, "a", "b"]
print(g.pop(2)) # Removes the item from the list and returns its value to the user
print(g)

# 11) List Repeat (*)
myList = [1, 2]
print(myList * 6)
