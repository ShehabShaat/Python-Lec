#  created by : shehab shaat 5/9/2022
# ===============================assignment 1======================================


values = (0, 1, 2)

if any(values):
    my_var = 0  # scope

my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]  # my_var is undefined , not global

# if all((my_list[:])): bad
# if all(my_list[:4]): good
# if  all(my_list[:6]): bad
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):  # good , because the my_list[:4]) is good

    print("Good")

else:

    print("Bad")

# good

# ===============================assignment 2======================================
v = 40

my_range = list(range(v))
#
# print(sum(my_range, v) + )  # 820
print(sum(my_range, v) + pow(v, v, v))
# pow(v, v, v) => (40^40)%40 => 0
# sum(my_range, v) => 40+sum(my_range)

# ===============================assignment 3======================================
n = 21
l = list(range(n))
if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
    print("Good")
# ============> short_if <============
print("Good" if round(sum(list(range(n))) / n) == max(0, 3, 10, 2, -100, -23, 9) else "bad")


# Output => Good
# ===============================assignment 4======================================
# my_all

def my_all(uList):
    return all(uList)


def my_any(uList):
    return any(uList)


def my_min(uList):
    return min(uList)


def my_max(uList):
    return max(uList)


print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False

# my_any
print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False

# my_min
print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700


# ====================================
