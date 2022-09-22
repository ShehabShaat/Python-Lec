peoples = {
    "SheHab": {
        "Python": "70%",
        "Kotlin": "80%",
        "Dart": "50%",
    },
    "Essam": {
        "Python": "60%",
        "Kotlin": "30%",
        "Dart": "80%",
    },
    "shAat": {
        "Python": "73%",
        "Kotlin": "0%",
        "Dart": "11%",
    }
}
# print(peoples["SheHab"])
# print(peoples["SheHab"]["Python"])
# print(peoples.get("SheHab"))
# print(peoples.values())
# print(peoples["SheHab"].values())
# print(peoples["SheHab"].keys())
# print(peoples["SheHab"])


for name in peoples:  # outer loop
    print(f'Skills and Progress For {name} Is : ')

    for skills in peoples[name]:
        print(f"{skills} => {peoples[name][skills]}")


else:
    print()

print("=" * 50)
myRang = range(1, 10)

# continue
for num in myRang:
    if num == 7:
        continue
    print(num)
print("=" * 50)

# break
for num in myRang:
    if num == 7:
        break
    print(num)
print("=" * 50)

# pass " بيعدي الليلة عشان ميعملش غلط "
for num in myRang:
    pass
for num in myRang:
    if num == 13:
        pass

    print(num)
