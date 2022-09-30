# ------------------------------------------------------
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run
# -------------------------------------------------------

import timeit

# print(dir(timeit))

print(timeit.timeit("'Elzero' * 1000"))

# name = "Elzero"
#
# print(name * 1000)

print(timeit.timeit("name = 'Elzero'; name * 1000"))  # ; => mean next new line statement

# print(random.randint(0, 50))

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))
