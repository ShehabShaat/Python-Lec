# --------------------
# -- Numpy => Intro --
# --------------------
# - NumPy Is A Python Third-Party Module To Deal With Arrays & Matrices
# - NumPy Stand For Numerical Python
# - NumPy Is Open Source
# - NumPy Support Dealing With Large Multidimensional Arrays & Matrices
# - NumPy Has Many Mathematical Functions To Deal With This Elements
# ------------------------------------------------------------
# * Why We Use NumPy Array
# - Consume Less Memory
# - Very Fast Compared To Python List
# - Easy To Use
# - Support Element Wise Operation
# - Elements Are Stored Contiguous
# -------------------------------------------
# * Python Lists
# ---- Homogeneous => Can Contains The Same Type of Objects
# ---- Heterogeneous => Can Contains Different Types of Objects.
# --------------------------------------------------------------
# - The Items in The Array Have to Be Of The Same Type
# - You Can Be Sure Whats The Storage Size Needed for The Array
# - NumPy Arrays Are Indexed From 0
# --------------------------------------------------------------
# - NumPy On Github => https://github.com/numpy/numpy
# ---------------------------------------------------

import numpy as np

print(np.__version__)
print("=" * 50)

# ========================================Create Arrays==========================================
myList = [1, 2, 3, 4, 5]
myArray = np.array(myList)
print(myList)
print(myArray)

print(type(myList))
print(type(myArray))
print("=" * 50)

# Accessing Elements

a = np.array(10)
b = np.array([10, 20])  # 1 diminution array
c = np.array([[1, 2], [3, 4]])  # 2 diminution array
d = np.array([[[5, 6], [7, 9]], [[1, 3], [4, 8]]])  # 3 diminution array

print(d[1][1][1])
print(d[1, 1, 1])
print(d[1, 1, -1])
# output => 8
print("=" * 50)

# Number Of Dimensions
print(a.ndim)  # ndim => number of diminutions
print(b.ndim)
print(c.ndim)
print(d.ndim)
print("=" * 50)

# Custom Dimensions
custom_array = np.array([1, 2, 3], ndmin=3)
print(custom_array[0])
print(custom_array[0][0])
print(custom_array[0][0][0])
print(custom_array[0, 0, 0])


# ========================================Compare Data Location And Type==========================================


import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array([1, 2, 3, 4, 5])

print(my_list[0])
print(my_list[1])

print(my_array[0])
print(my_array[1])

print("#" * 50)

print(id(my_list[0]))
print(id(my_list[1]))

print(id(my_array[0]))
print(id(my_array[1]))

print("#" * 50)

my_list_of_data = [1, 2, "A", "B", True, 10.50]
my_array_of_data = np.array([1, 2, "A", "B", True, 10.50])

print(my_list_of_data)
print(my_array_of_data)

print("#" * 50)

print(my_list_of_data[0])
print(my_array_of_data[0])

print(type(my_list_of_data[0]))
print(type(my_array_of_data[0]))

print("#" * 50)

my_list_of_data_two = [1, 2, "A", "B", True, 10.50]
my_array_of_data_two = np.array([1, 2, "A"])

print(my_list_of_data_two)
print(my_array_of_data_two)

print("#" * 50)

print(my_list_of_data_two[0])
print(my_array_of_data_two[0])

print(type(my_list_of_data_two[0]))
print(type(my_array_of_data_two[0]))