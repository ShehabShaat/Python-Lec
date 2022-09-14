# created by : shehab shaat 14/9/2022

# ===============================assignment 1======================================
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

final_string = ""
for data in zip(my_list, my_tuple):
    final_string += "".join(data).lower()
    if data[0]:
        final_string = final_string.replace(final_string[0], final_string[0].upper(), 1)

print(final_string)

# ===============================assignment 2======================================

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

final_string = ""
for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if str(item1).isalpha():
        final_string += "".join(item1).lower()
        if item1[0]:
            final_string = final_string.replace(final_string[0], final_string[0].upper(), 1)
    else:
        continue
print(final_string)
# ===============================assignment 3======================================
from PIL import Image

# open Image()
my_image = Image.open("files/elzero-pillow1.png")

# crop image
my_box = (400, 0, 800, 400)  # left , upper ,right ,lower
my_crop = my_image.crop(my_box)

# convert mode image
my_convert = my_crop.convert("L")

# show image
my_convert.show()
# sava image
my_convert.save("files/L.png")

# rotate image
my_rotate = my_image.rotate(180)
my_rotate.save('files/rotate.png')

my_box1 = (0, 0, 1200, 400)  # left , upper ,right ,lower
my_crop2 = my_rotate.crop(my_box1)
my_crop2.save('files/rotate-crop.png')

my_convert2 = my_crop2.convert("L")
my_convert2.show()
my_convert2.save('files/rotate-convert.png')


# ===============================assignment 4======================================

def say_hello_to(name):
    """
    parameter(someone) => Person Name
    Function To Say Hello To Anyone
    """
    return f"Hello {name}"


print(say_hello_to("shehab"))
print(say_hello_to.__doc__)

# ===============================assignment 5======================================
''' this file to test pylint '''
myFriends = ["Ahmed", "Osama", "Sayed"]


def say_hello(some_peoples) -> list:
    """this function to print hello any someone in the list"""
    for someone in some_peoples:
        print(f"Hello {someone}")


say_hello(myFriends)
# output
# Your code has been rated at 10.00/10 (previous run: 0.00/10, +10.00)
