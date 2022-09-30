# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------

class BaseOne:

    def __init__(self):
        print("Base One")

    @staticmethod
    def func_one():
        print("One")


class BaseTwo:

    def __init__(self):
        print("Base Two")

    @staticmethod
    def func_two():
        print("Two")


class Derived(BaseOne, BaseTwo):
    pass


myVar = Derived()
