import string, random

# print(string.digits);print(string.ascii_letters);print(string.ascii_lowercase)
import timeit

myList = []


def Generate_serial(count):
    all_char = string.ascii_letters + string.digits

    for _ in range(count):
        myList.append(all_char[random.randint(0, len(all_char) - 1)])

    return "".join(myList)


print(Generate_serial(14))
