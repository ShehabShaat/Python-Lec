# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------

class BaseOne:

    def __init__(self):
        print("Base One")

    def func_one(self):
        print("One")


class BaseTwo:

    def __init__(self):
        print("Base Two")

    def func_two(self):
        print("Two")


class Derived(BaseOne, BaseTwo):
    pass


myVar = Derived()
