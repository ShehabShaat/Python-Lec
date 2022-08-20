# While and Else
a = 0
while a < 10:
    print("I love Python")
    a += 1

else:
    print("loop is done")  # true become false

# while False:  error because the condition is False
# print("Will not print")  error because the condition is False
print("=" * 50)
myList = ["A", "B", "C", "D", "E", "F", "G", "J", "K", "L"]
b = 0
while b < len(myList):
    print(f"#{str(b+1).zfill(2)} {myList[b]}")
    b += 1


