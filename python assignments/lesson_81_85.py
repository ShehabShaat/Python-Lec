# created by : shehab shaat 11/9/2022

# ===============================assignment 1======================================
def reverse_string(my_string):
    yield my_string


res = reverse_string("El-zero")
print(next(res))
# Reverse The String
for c in reverse_string("El-zero"):
    print(c)


# ===============================assignment 2======================================
def my_decorator(fun):
    def nested_decorator():
        print("Sugar Added From Decorators")
        fun()
        print("####################")

    return nested_decorator


@my_decorator
def make_tea():
    print("Tea Created")


@my_decorator
def make_coffee():
    print("Coffee Created")


make_tea()
make_coffee()
