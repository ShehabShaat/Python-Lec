# created by :shehab shaat  16/8/2022
# ===============================assignment 2======================================

my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
unique_list = list(unique_list)
print(unique_list)
print(type(unique_list))
unique_list.pop(-1)
print(unique_list)
print("=" * 50)

# ===============================assignment 2======================================
nums = {1, 2, 3}
letters = {"A", "B", "C"}

nums.update(letters)
print(nums)

nums.union(letters)
print(nums)

nums = list(nums)
nums.extend(letters)
nums = set(nums)
print(nums)
print("=" * 50)
# ===============================assignment 3======================================
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)

my_set.clear()
print(my_set)

my_set.add("A")
my_set.add("B")
print(my_set)

my_set.discard("C")
print(my_set)
print("=" * 50)

# ===============================assignment 4======================================
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print("="*50)
# ===============================assignment 5======================================

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

print(language["one"]["name"] + " Progress Is " + language["one"]["progress"])
print(language["two"]["name"] + " Progress Is " + language["two"]["progress"])
print(language["three"]["name"] + " Progress Is " + language["three"]["progress"])

language.update({"four": {"name": "Dart", "progress": "30%"}})
print(language["four"]["name"] + " Progress Is " + language["four"]["progress"])
