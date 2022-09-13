def myDecorator(fun):
    def nestedDecorator(*number):
        for num in number:
            if num < 0:
                print(f"Beware : {num} < 0")
                fun(*number)

    return nestedDecorator


@myDecorator
def calculate(n1, n2, n3):
    print(n1 + n2 + n3)


calculate(-1, 1, 5)

# ===============================================================================================
from time import time


# speed test
def speed_test(fun):
    def wrapper():
        start = time()
        fun()
        end = time()
        print(f"Function Running Is : {end - start}")

    return wrapper


myList = []
for _ in range(1000000):
    myList.append(_)


@speed_test
def bigRange():
    for _ in myList:
        print(_)


bigRange()
