# -------------------------
# -- Function And Return --
# -------------------------
# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps
# ----------------------------------------

def fun_name():
    # print("Hello Function")
    return "Hello Function"


#
# fun_name()
print(fun_name())


# Function Parameters + Arguments

def say_Hello(name):
    print(f"Hello {name}")


def addition(n1, n2):
    if type(n1) != int or type(n2) != int:

        print("Please enter only numbers..")

    else:
        print(n1 + n2)


def fullName(first, middle, last):
    print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")


#
#
say_Hello("sheHab")
addition(1, "ds")
#
first = input("Enter First Name : ")
middle = input("Enter First Name : ")
last = input("Enter First Name : ")
fullName(first, middle, last)
