a = ("s", "h", "e", "h", "a", "b")

print(a)
a = "s", "h", "e", "h", "a", "b", "s", "h", "a", "a", "t"
print(a)
print(a[1:4:1])
print(a[1] + "\n" + a[-1] + "\n" + a[-3])
# tuples ar immutable (cannot edit element but you can delete or add element
# a[1]="S" error
'================================Tuples And Methods================================'
a = "sh",

print(type(a))
a = ("sh",)
print(type(a))
print(len(a))

# tuples concatenation
b = 5, 6
c = a + b + ("A", "B")
print(c)
print(type(c))
# Tuple, list ,  Repeat (*)

myString = "shehab"
myList = [1, 2]
myTuple = ("A", "B")
print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# count
a = 1, 2, 3, 4, 5, 5
print(a.count(5))
print("the position of index is : {:d}".format(a.index(5)))

# Tuple Destruct

a = ("A", "B", "C")
x, y, z = a
print(x)
print(y)
print(z)
a = ("A", "B", 3, "C")
x, y, _, z = a # ignor 3
print(x)
print(y)
print(z)
