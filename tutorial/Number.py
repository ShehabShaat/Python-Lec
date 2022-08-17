# Integer
print(type(1))
print(type(10))
print(type(100))
print(type(-10))
print(type(-100))
# float
print(type(1.0))
print(type(10.4))
print(type(100.500))
print(type(-10.0))
print(type(-0.5))
# Complex
print(type(5 + 6j))
print(type(5 - 6j))
complexNumber = 5 + 6j
print("this is complex number {} ".format(complexNumber) + "real part is : {}"
      .format(complexNumber.real) + " imag part is : {}".format(complexNumber.imag))

# Notes
# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(int(5.0))
# print(int(5+5j)) error can't convert complex to int
print(float(5))
# print(float(5+6j)) error can't convert complex to float
print(complex(5))
print(complex(5.3))
