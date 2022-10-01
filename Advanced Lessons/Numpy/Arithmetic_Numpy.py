import numpy as np

my_array1 = np.array([10, 20, 30])
my_array2 = np.array([10, 50, 60])
print(my_array1 + my_array2)
print(my_array1 - my_array2)
print(my_array1 * my_array2)
print(my_array1 / my_array2)

print("=" * 50)
my_array3 = np.array([[10, 20], [30, 40]])
my_array4 = np.array([[10, 40], [60, 10]])
print(my_array3 + my_array4)
print(my_array3 - my_array4)
print(my_array3 * my_array4)
print(my_array3 / my_array4)

print("=" * 50)
print(my_array1)
print(my_array1.max())
print(my_array1.min())
print(my_array1.sum())

print("=" * 50)
print(my_array3)
print(my_array3.max())
print(my_array3.min())
print(my_array3.sum())

print("="*50)
# Ravel

my_array7 = np.array([[6, 4], [3, 9]])
print(my_array7.ravel())

my_array8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(my_array8.ndim)
print(my_array8.ravel())
x = my_array8.ravel()
print(x.ndim)