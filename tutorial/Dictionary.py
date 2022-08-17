# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces {}
# [2] Dict Items Are Contains "Key : Value"
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------
users = {"name": "shehab shaat",
         "job": "software Engineer",

         "country": "palestine",
         "skills": ["Kotlin", "Java", "C++", "Python"],
         "Rating": 4.7,

         # (1, 2, 3, 4): "test",
         # [1,2,3] :"test"  error
         # "test": [1, 2, 3]
         }
users_copy = users.copy()
print(users)
print("=" * 100)
print(users['country'])
print(users.get("country"))
print("=" * 100)
print(users.keys())  # "print all keys"
print(users.values())  # "print all values
print("=" * 100)

# Two diminution dictionary
language = {
    "one": {
        "name": "Python",
        "progress": "90%"
    },
    "two": {
        "name": "Kotlin",
        "progress": "80%"
    },
    "three": {
        "name": "C++",
        "progress": "85%"
    }

}
print(language)
print("=" * 100)
print(language['one'])
print("=" * 100)

print(language['two']['progress'])
print(language['two']['name'])

print("=" * 100)
print(len(language["two"]))

frameworkOne = {

    "name": "Laravel",
    "progress": "0%"
}

frameworkTow = {
    "name": "Django",
    "progress": "80%"

}

frameworkThree = {

    "name": "Laravel",
    "progress": "0%"
}
print("=" * 100)
allFrameworks = {

    "one": frameworkOne,
    "two": frameworkTow,
    "three": frameworkThree
}
print(allFrameworks["one"])
print(allFrameworks["one"]['name'])
print(len(allFrameworks["one"]['progress']))
print("=" * 100)
"==============================================Dictionary Method =============================================="
# clear()
print(users)
users.clear()
print(users)
print("=" * 100)

# update()
users_copy["github"] = "https://github.com/ShehabShaat"
print(users_copy)
users_copy.update({"collage": "ptc"})
print(users_copy)
print("=" * 100)
print(users_copy.keys())
print(users_copy.values())
print("=" * 100)

users_copy.setdefault("age", 22)
print(users_copy)
print("=" * 100)
# popitem()
member = {
    "name": "Shehab",
    "skill": "Python",
}
print(member)
member.update({"age": 22})
print(member.popitem())  # return last element in the dict
print("=" * 100)
# items()
allItems = member.items()
print(allItems)
member["age"] = 36
print(allItems)
print("=" * 100)

# fromkeys()
a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')  # keys
b = "X" # value keys
print(dict.fromkeys(a, b))
print(type(dict.fromkeys(a, b)))
