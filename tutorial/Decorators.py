# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)

def my_decorator1(fun):
    def my_nested_my_decorator():
        print("before")
        fun()
        print("after")

    return my_nested_my_decorator


@my_decorator1
def my_fun1():
    print("text")


def my_fun2():
    print("text")


my_fun1()
print("=" * 50)
my_fun2()
print("=" * 50)


# ================================Decorators - Function With Parameters=================
def my_decorator2(fun):
    def my_nested_my_decorator2(n1, n2):
        if n1 < 0 or n2 > 100:
            print("Beware the num 1 or 2 undefined ")
        fun(n1, n2)

    return my_nested_my_decorator2


# =========================================================================
def my_decorator3(func):  # Decorator

    def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

        print("Coming From Decorator three")

        func(num1, num2)  # Execute Function

    return nestedFunc  # Return All Data


@my_decorator3
@my_decorator2
def calculate(n1, n2):
    print(n1 + n2)


calculate(-1, 2)  #
