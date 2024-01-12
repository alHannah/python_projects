# """Time: 25mins"""
# import colorgram
#
# img_color = colorgram.extract("duck.jpg", 6)
#
# color_list = []
# for every_color in img_color:
#     r = every_color.rgb.r
#     g = every_color.rgb.g
#     b = every_color.rgb.b
#     tuple_rgb_color_format = (r, g, b)
#     color_list.append(tuple_rgb_color_format)

import turtle
import random

fin = turtle.Turtle()
turtle.colormode(255)
window = turtle.Screen()
fin.speed("fastest")


color_list = [(126, 88, 53), (70, 42, 26), (163, 143, 108), (162, 132, 79), (106, 49, 30), (99, 59, 25)]


# for dot in range(2):
#     fin.color(dot_color())
#     fin.begin_fill()
#     fin.circle(20)
#     fin.end_fill()
def paint(length):
    # rotate = 0
    for t in range(length):
        for _ in range(length):
            fin.setheading(0)
            fin.dot(20, random.choice(color_list))
            fin.penup()
            fin.fd(50)
        fin.setheading(90)
        fin.fd(30)
        fin.setheading(180)
        fin.fd(length * 50)
        fin.pendown()
        # rotate += 1


paint(10)



window.exitonclick()
