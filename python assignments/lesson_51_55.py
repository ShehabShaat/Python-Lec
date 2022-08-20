# # created by : shehab shaat 20/8/2022
#
# # ===============================assignment 1======================================
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
count = 0
for index in my_nums:
    if index % 5 == 0:
        count += 1
        print(f"{count} => {str(index)}")

print("All Numbers Printed")
print("=" * 50)

# # ===============================assignment 2======================================
#
myRange = range(1, 21)
myList = [6, 8, 12]
for num in myRange:
    if num in myList:
        continue
    print(f"{str(num).zfill(2)}")

print("All Numbers Printed")
print("=" * 50)
# ===============================assignment 3======================================

my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
total = 0
for key, value in my_ranks.items():
    if value == "A":
        print(f"My Rank in {key} Is {value} And This Equal 100 Points")
        total += 100
    elif value == "B":
        print(f"My Rank in {key} Is {value} And This Equal 80 Points")
        total += 80
    else:
        print(f"My Rank in {key} Is {value} And This Equal 40 Points")
        total += 40

print(f"Total Points Is {total}")

# ===============================assignment 4======================================
print("=" * 50)

students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}
for key in students:
    print("-" * 50)
    print(f"Student Name => {key} : ")
    print("-" * 50)
    totalMarks = 0

    for value in students[key]:

        if students[key][value] == "A":
            print(f"{value} => 100 Points")
            totalMarks += 100
        elif students[key][value] == "B":
            print(f"{value} => 80 Points")
            totalMarks += 80
        elif students[key][value] == "C":
            print(f"{value} => 40 Points")
            totalMarks += 40
        else:
            print(f"{value} => 20 Points")
            totalMarks += 20

    print(f"Total Points For {key} Is {totalMarks}")
print(" New Method ".center(100, "#"))

for k, v in students.items():
    print("-" * 50)
    print(f"Student Name => {k} : ")
    print("-" * 50)
    totalMarksNew = 0
    for main_K, main_v in v.items():
        if main_v == "A":
            print(f"{main_K} => 100 Points")
            totalMarksNew += 100
        elif main_v == "B":
            print(f"{main_K} => 80 Points")
            totalMarksNew += 80

        elif main_v == "C":
            print(f"{main_K} => 40 Points")
            totalMarksNew += 40

        else:
            print(f"{main_K} => 20 Points")
            totalMarksNew += 20

    print(f"Total Points For {k} Is {totalMarksNew}")
