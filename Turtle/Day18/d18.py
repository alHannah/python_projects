from turtle import *
from random import  *

my_turtle = Turtle()
window = Screen()
my_turtle.color("black")
my_turtle.shape("turtle")
my_turtle.pensize(10)
# my_turtle.turtlesize(10)
my_turtle.speed(250)


# def draw(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
#
#
# for ink in range(3, 11):
#     my_turtle.color(random.random(), random.random(), random.random(),)
#     draw(ink)

# def create_path():
#     walk = [
#         my_turtle.left(90),
#         my_turtle.right(90)
#     ]
#
#     return random.choice(walk)
#
#
# for _ in range(1, 50):
#     my_turtle.forward(100)
#     create_path()
#     my_turtle.backward(100)
#     my_turtle.color(random.random(), random.random(), random.random(),)


# def left():
#     my_turtle.left(90)
#
#
# def right():
#     my_turtle.right(90)
#
#
# def forward():
#     my_turtle.forward(100)
#
#
# def backward():
#     my_turtle.backward(100)
#
#
# move = [left(), right(), forward(), backward()]
#
# for _ in range(100):
#     choice(move)
#     my_turtle.color(random(), random(), random(), )
#     print(choice(move))
#     print(my_turtle.position())

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)

# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break

direction = [0, 90, 180, 270]

for i in range(100):
    my_turtle.color(random(), random(), random())
    my_turtle.setheading(choice(direction))
    my_turtle.forward(100)


window.exitonclick()
