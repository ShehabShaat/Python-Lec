# ------------------------------
# for item in iterable_object
#        Do Something with Item
# ------------------------------
a = 1
myList = []
evenNumber = []
oddNumber = []

while a <= 10:
    myList.append(a)
    a += 1
else:
    print()

for number in myList:
    # print(str(number).zfill(2))

    if number % 2 == 0:
        evenNumber.append(str(number).zfill(2))
        print(f"The Number {number} Is Even")

    else:
        print(f"The Number {number} Is Odd")
        oddNumber.append(str(number).zfill(2))
else:
    print("finished loop")
print("=" * 50)
print(f"Even Number : {evenNumber}\nOdd Number : {oddNumber}")
print("=" * 50)
myname = input("Enter your name :").strip().upper()
for letter in myname:
    print(f"[ {letter} ]")

print("=" * 50)
myRang = range(1, 100)
for num in myRang:
    print(num)

skills = {
    "Kotlin": "60%",
    "Python": "80%",
    "Java": "90%",
    "c++": "85%"
}

for skill in skills:
    print(f"My Progress in Lang {skill} IS : {skills[skill]}")
    # print(f"My Progress in Lang {skill} IS : {skills.get(skill)}")
