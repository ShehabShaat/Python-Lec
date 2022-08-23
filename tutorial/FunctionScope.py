# --------------------
# -- Function Scope --
# --------------------

x = 1  # Global Scope


def one():
    global x  # override
    x = 2
    print(f"Print Variable From Function Scope {x}")


def two():
    x = 10
    print(f"Print Variable From Function Scope {x}")


print(f"Print Variable From Global Scope {x}")
one()
print(f"Print Variable From Global Scope {x}")
two()
print(f"Print Variable From Global Scope After One Function Is Called {x}")
