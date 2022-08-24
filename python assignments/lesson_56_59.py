#  created by : shehab shaat 24/8/2022
# ===============================assignment 1======================================

def calculate(num1, num2, operator="+"):
    if operator == "A" or operator == "+":
        return num1 + num2
    elif operator == "S" or operator == "-":
        return num1 - num2
    elif operator == "M" or operator == "*":
        return num1 * num2
    else:
        return "This process does not exist"


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
operator = input("Enter type operator [+ , - , * ]: ").capitalize()

print(calculate(num1, num2, f"{operator:.1}"))  # case 1

print(calculate(num1, num2))  # case 2


# ===============================assignment 2======================================
def addition(*num):
    sum = 0
    for s in num:
        if s == 10:
            continue
        elif s == 5:
            sum -= 5
        else:
            sum += s

    return sum


print(addition(10, 20, 30, 10, 15, 5, 100))
print(addition(10, 20, 30, 10, 15))


# ===============================assignment 3======================================

def show_skills(name, *skills):
    if len(skills) == 0:
        print(f"Hello {name} You Have No Skills To Show")
    else:
        print(f"Hello {name} Your Skills Is :")
        for skill in skills:
            print(f"- {skill}")


show_skills("SheHab", "HTML", "CSS", "JS", "Python")
show_skills("SheHab")


# ===============================assignment 4======================================

def say_hello(name="unKnown", age="unKnown", country="unKnown"):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"


age = int(input("Enter age : "))

print(say_hello())
print(say_hello("sheHab", "Palestine"))
