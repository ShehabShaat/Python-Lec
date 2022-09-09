import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch
from matplotlib.patches import Polygon
from matplotlib import pyplot as plt, patches

# Plotting the tri colours in national flag
a = patch.Rectangle((0, 1), width=12, height=2, facecolor='green', edgecolor='green')
b = patch.Rectangle((0, 3), width=12, height=2, facecolor='white', edgecolor='white')
c = patch.Rectangle((0, 5), width=12, height=2, facecolor='black', edgecolor='black')

e = patch.Rectangle((0, 1), width=3, height=2, facecolor='white', edgecolor='white')
ee = patch.Rectangle((-2, 1), width=2, height=2, facecolor='white', edgecolor='white')
eee = patch.Rectangle((-2, -1), width=2, height=16, facecolor='white', edgecolor='white')

d = patch.Rectangle((0, 3), width=3, height=2, facecolor='white', edgecolor='white')
dd = patch.Rectangle((-2, 3), width=3, height=2, facecolor='white', edgecolor='white')

f = patch.Rectangle((0, 5), width=3, height=2.5, facecolor='white', edgecolor='white')
ff = patch.Rectangle((-2, 5), width=3, height=2, facecolor='white', edgecolor='white')

py.rcParams["figure.figsize"] = [7.00, 5.50]
py.rcParams["figure.autolayout"] = True
rectangle = patches.Rectangle((2.5, 0.25), 5, 5, edgecolor='red',
                              facecolor="red", linewidth=0, angle=45)

m, n = py.subplots(1)

n.add_patch(a)
n.add_patch(b)
n.add_patch(c)

n.add_patch(rectangle)
n.add_patch(e)
n.add_patch(ee)
n.add_patch(eee)
n.add_patch(d)
n.add_patch(dd)
n.add_patch(f)
n.add_patch(ff)
py.axis('equal')
py.show()


# from turtle import *
#
# speed(8)
# setup(800, 400)
# penup()
# goto(-400, 200)
# pendown()
#
# # black recangle
# color("black")
# begin_fill()
# forward(800)
# right(90)
# forward(133)
# right(90)
# forward(800)
# right(180)
# end_fill()
#
# # whie recangle
# color("white")
# begin_fill()
# forward(800)
# right(90)
# forward(133)
# right(90)
# forward(800)
# right(180)
# end_fill()
#
# # green recangle
# color("green")
# begin_fill()
# forward(800)
# right(90)
# forward(133)
# right(90)
# forward(800)
# right(180)
# end_fill()
#
# # red recangle
# color("red")
# begin_fill()
# goto(-255,30)
# left(310)
# forward(-410)
# end_fill()
#
# mainloop()
