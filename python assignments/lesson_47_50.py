# # created by : shehab shaat 20/8/2022
#
# # ===============================assignment 1======================================
num = int(input("Enter number : ").capitalize().strip())
# print(type(num)) # <class 'int'>
count = 0

if num > 0:
    while num > 0:
        num -= 1
        if num == 0:
            break
        print(num)
        count += 1

else:
    print("Number 0 Is Not Larger Than 0")

print(f"{count} Numbers Printed Successfully.")
print("=" * 50)

# # ===============================assignment 2======================================

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
num, index = len(friends), 0

while index < num:
    if friends[index].istitle():
        print(friends[index])
        count += 1
    index += 1

print(f"Friends Printed And Ignored Names Count Is {num - count}")

print("=" * 50)

# # ===============================assignment 3======================================

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print(skills.pop(0))
# # ===============================assignment 4======================================
my_friends = []
numberFriend = 4

while numberFriend > 0:
    name = input("Enter Your fined : ").strip()
    if name.isupper():
        print("Invalid Name")
    elif name.islower():
        my_friends.append(name.capitalize())
        print(f"Friend {name} Added => 1st Letter Become Capital")
        numberFriend -= 1
        print(f"Names Left in List Is {numberFriend}" if numberFriend != 0 else "List is Full")

    elif name.capitalize():
        my_friends.append(name)
        print(f"Friend {name} Added")
        numberFriend -= 1
        print(f"Names Left in List Is {numberFriend}" if numberFriend != 0 else "List is Full")

    else:
        pass

print(my_friends)
