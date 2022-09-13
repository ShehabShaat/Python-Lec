from PIL import Image

# [review]https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
# open image from your path
my_image = Image.open('files/img.png')
# show image
my_image.show()
myBox = (0, 0, 800, 800)  # left , upper ,right ,lower
my_new_image = my_image.crop(myBox)
my_new_image.show()
# convert mode image

myConvertedImage = my_image.convert("L")
myConvertedImage.show()

