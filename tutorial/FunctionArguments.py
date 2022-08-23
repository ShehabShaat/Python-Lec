# Function Arguments packing , unpacking *Args
print(1, 2, 3, 4)
myList = [1, 2, 3, 4]
print(myList)
print(*myList)


def say_hello(n1, n2, n3, n4):
    peoples = [n1, n2, n3, n4]
    for name in peoples:
        print(f"{name}")


def say_hello_(*peoples):
    # print(type(peoples)) tuple
    for name in peoples:
        print(f"{name}")


say_hello("shehab", "esaam", "Shaat", "boood")
print("=" * 50)
say_hello_("shehab", "esaam", "Shaat", "boood", "Ali")
print("=" * 50)


def show_details(name, *skills):
    print(f"hello {name} Your Skills Is : ")
    for names in skills:
        print(f" {names}", end="")

    print()


show_details("shehab", "Python", "C++", "Java", "Kotlin")
# =====================================================================================
print("=" * 50)

# Function Arguments packing , unpacking **Args

my_dict = {
    "Kotlin": "80%",
    "java": "80%",
    "Python": "70%",
    "C++": "70%"
}


def say_hello1(**people):
    # print(type(peoples)) dict
    for key, value in people.items():
        print(f"{key} => {value}")


say_hello1(Python="70%", kotlin="80%")
print("="*50)
say_hello1(**my_dict)
