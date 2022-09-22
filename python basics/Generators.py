# yield Produce Data
# Generator is a Function With "yield" Keyword Instead of "return"
# It Supports Iteration and Return Generator Iterator By Calling "yield"
# Generator Function Can Have one or More "yield"
#  When Called, It's Not Start Automatically, Its Only Give You The Control

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


print(type(myGenerator()))  # <class 'generator'>
res = myGenerator()
print(next(res))
print("Hello GSG")
print(next(res))
print("Hello GSG")
print(next(res))
print("Hello GSG")
print(next(res))

for num in res:
    print(num)
