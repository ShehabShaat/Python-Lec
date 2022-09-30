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
    def __init__(self):
        BaseOne.__init__(self)
        BaseTwo.__init__(self)


myVar = Derived()
