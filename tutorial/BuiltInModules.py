# import random
#
# print(f"random flouting number {round(random.random())}")
# print(random)
# print(dir(random))


from random import randint, randrange, random

print(f"Print Random Range {randrange(0, 10)}")
print(f"Print Random Integer {randint(0, 10)}")
print(f"Print Random Flout {random()}")
print("=" * 50)
# ======================================create your module====================================================


import shehab as sh, sys

print(sys.path)
# sys.path.append(r"C:\Users\shehab\Desktop\Python Toturial\tutorial\shehab.py'")

print(sh)
print(dir(sh))
sh.myName()
