def say_hello_(name, age="unKnown", country="unKnown"): # الديفولت لازم يكون اخر شي
    # say_hello_(name = "unKnown", age="unKnown", country="unKnown"): no error
    # say_hello_(name = "unKnown", age, country): error
    print(f"{name} {age} {country}")


say_hello_("shaat")
say_hello_("shaat","22")
