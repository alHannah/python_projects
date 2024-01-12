import random
from turtle import *
from random import *

my_turtle = Turtle()
window = Screen()
my_turtle.color("cyan")
my_turtle.shape("turtle")
# my_turtle.pensize(5)
my_turtle.speed("fastest")

#
# def square(distance, angle):
#     line = 0
#     while line != 4:
#         my_turtle.forward(distance)
#         my_turtle.left(angle)
#         line += 1
#
#
# def dash_line():
#     for dash in range(20):
#         my_turtle.pd()
#         my_turtle.forward(10)
#         my_turtle.pu()
#         my_turtle.forward(10)


# from 3 sides to 10
# angle = 360 / sides
# random color


# def draw_shape(dist, angles):
# shape_side = 3
# for every_turn in range(shape_side):
#     my_turtle.forward(dist)
#     my_turtle.right(angles)
#     shape_side += 1

# shapes = [
#     {"shape": 3},
#     {"shape": 4},
#     {"shape": 5},
#     {"shape": 6},
#     {"shape": 7},
#     {"shape": 8},
#     {"shape": 9},
#     {"shape": 10},
# ]
#
# color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'cyan', 'black', 'white']
#
# line = 3
# for sides in shapes:
#     degree = 360 / line
#     line += 1
#     shape_degree = int(degree)
#     sides["degree"] = shape_degree
#
# done = 0
# for turns in shapes:
#     line = turns["shape"]
#     curve = turns["degree"]
#
#     while line != done:
#         my_turtle.forward(100)
#         my_turtle.right(curve)
#         done += 1
#
#     done = 0
#     any_color = choice(color)
#     my_turtle.color(any_color)
#
# for _ in range(10):
#     choose_side = [my_turtle.left(90), my_turtle.right(90)]
#     choose_move = [my_turtle.forward(100), my_turtle.backward(100)]
#     choice(choose_side)
#     choice(choose_move)
#     my_turtle.color(random(), random(), random(), )

def dot_color():
    color_list = [(126, 88, 53), (70, 42, 26), (163, 143, 108), (162, 132, 79), (106, 49, 30), (99, 59, 25)]
    f_color = color_list[randint(0, len(color_list))]
    return f_color
def tri_color():
    r = random()
    g = random()
    b = random()
    fav_color = (r, g, b)
    return fav_color


for i in range(40):
    # t_color = ("magenta", "cyan", "yellow")
    my_turtle.color(dot_color())
    my_turtle.tilt(30)
    my_turtle.setheading(i * 20)
    # for _ in range(i):
    my_turtle.circle(90)
    print(dot_color())
"""Time: 25 mins"""

    

# square(50, 90)
# dash_line()
window.exitonclick()

