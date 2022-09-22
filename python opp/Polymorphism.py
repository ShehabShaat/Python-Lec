# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------

class A:

    def do_something(self):
        print("From Class A")

        raise NotImplementedError("Derived Class Must Implement This Method")


class B(A):

    def do_something(self):
        print("From Class B")


class C(A):

    def do_something(self):
        print("From Class C")


my_instance = B()
my_instance.do_something()
