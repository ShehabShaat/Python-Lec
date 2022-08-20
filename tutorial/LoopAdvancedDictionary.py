
skills = {
    "Kotlin": "60%",
    "Python": "80%",
    "Java": "90%",
    "c++": "85%"
}
# print(skills.items())
for skill in skills:
    print(f"{skill} => {skills[skill]}")
print("=" * 50)

for key, value in skills.items():
    print(f"{key} => {value}")


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
for key, value in peoples.items():
    print(f"{key} Progress is : ")
    for child_Key,child_Value in value.items():
        print(f"- {child_Key} => {child_Value}")
