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
print(round(155.555,2))
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