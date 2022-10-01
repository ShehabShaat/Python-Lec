# -- Numpy => Array Slicing --

import numpy as np

# Slicing => [Start:End:Steps] Not Including End

a = np.array(["A", "B", "C", "D", "E", "F"])
c = np.array([['A', 'B'], ['C', 'D'], ['E', 'F']])
e = np.array([[[5, 6], [7, 9]], [[1, 3], [4, 8]]])  # 3 diminution array

print(a.ndim)
print(c.ndim)
print(e.ndim)
print(a[1])
print(a[1:4])
print(a[:4])
print(a[2:])
#
print("#" * 50)

b = np.array([["A", "B", "X"], ["C", "D", "Y"], ["E", "F", "Z"], ["M", "N", "O"]])
#
print(b.ndim)
print(b[1])
print("#" * 50)
print(b[2:, :2])
print(b[2:, :2:2])
print("#" * 50)
d = np.array([[['A', 'B'], ['C', 'D']], [['J', 'H'], ['K', 'L']], [['J', 'H'], ['K', 'L']]])

print(d.ndim)
print(d[1])
print(d[0][1][1])

print(d[2:, :1, -1])
print(d[2:, :1, -1][0])
print(d[2:, :1, -1][0][0])
