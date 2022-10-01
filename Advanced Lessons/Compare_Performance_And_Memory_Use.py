# -------------------------------------------------
# -- Numpy => Compare Performance And Memory Use --
# -------------------------------------------------
# - Performance
# - Memory Use
# -------------------------------------------------

import numpy as np
import time
import sys

elements = 150000

my_list1 = range(elements)
my_list2 = range(elements)

my_array1 = np.arange(elements)
my_array2 = np.arange(elements)

list_start = time.time()
list_result = [(n1 + n2) for n1, n2 in zip(my_list1, my_list2)]
print(f"List Time: {time.time() - list_start}")

array_start = time.time()
array_result = my_array1 + my_array2
print(f"Array Time: {time.time() - array_start}")

# for n1, n2 in zip(my_list1, my_list2):

# 	print(n1 + n2)

print(list_result)
print(array_result)

my_array = np.arange(100)

print(my_array)
print(my_array.itemsize)
print(my_array.size)
print(f"All Bytes: {my_array.itemsize * my_array.size}")

print("#" * 50)

my_list = range(100)
print(sys.getsizeof(1))
print(len(my_list))
print(f"All Bytes: {sys.getsizeof(1) * len(my_list)}")