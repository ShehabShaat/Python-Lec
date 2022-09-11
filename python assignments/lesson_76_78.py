# created by : shehab shaat 11/9/2022

# ===============================assignment 1======================================
import random

print(f"Random Number Between 10 And 50 => {random.randint(10, 50)}")
print(f"Random Even Number Between 2 And 10 =>{random.randrange(2, 10, 2)}")
print(f"Random Odd Number Between 1 And 9 =>{random.randrange(1, 9, 2)}")
print(dir(random))
# ===============================assignment 2======================================
from Python import my_mod
my_mod.say_hello("shehab")
my_mod.say_welcome("shehab")
print(dir(my_mod))
# ===============================assignment 4======================================

my_mod.say_welcome("shehab")

# ===============================assignment 4======================================
new_wellcome = my_mod.say_welcome("shehab")
print(new_wellcome)
