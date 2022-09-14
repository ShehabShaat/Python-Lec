
# created by : shehab shaat 14/8/2022

# ===============================assignment 1======================================

NUM = input("Add Your Number ")
if len(NUM) > 1:
    raise Exception("IndexError: Only One Character Allowed")

if int(NUM) > 0:
    print(f"The Number Is {NUM}")
else:
    raise Exception("ValueError: Number Must Be Larger Than 0")

# ===============================assignment 2======================================

LETTER = str(input("Add Letter From A to Z : "))
my_list = []
for i in range(65, 91):
    my_list.append(chr(i))

try:
    if LETTER not in my_list:
        if len(LETTER) > 1:
            raise IndexError
        elif LETTER.isdigit():
            raise TypeError
        raise IOError


except IOError:
    print("The Letter Not In A - Z")

except IndexError:
    print("You Must Write One Character Only")
except TypeError:
    print("You Must Write Character Only")
else:
    print(f"You Typed {LETTER}")


# ===============================assignment 3======================================
def calculate(num1, num2) -> int:
    return num1 + num2


print(calculate(20, 30))
