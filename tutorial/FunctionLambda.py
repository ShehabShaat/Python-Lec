def say_hello(name, age): return f"hello {name} your Age is : {age}"


Hello = lambda names, age: f"hello {names} your Age is : {age}"

print(say_hello("sheHab", 22))
print(Hello("shaAt", 22))
print(say_hello.__name__)
print(Hello.__name__)

print(type(Hello))
