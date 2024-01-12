import turtle
import random

t = turtle.Turtle()
window = turtle.Screen()
t.hideturtle()
t.speed("fastest")

t.heading()


def draw_tree():
    for _ in range(50):
        t.color(random.random(), random.random(), random.random())
        t.fd(50)
        t.setheading(90)
        t.fd(5)
        t.setheading(180)
        t.fd(50)
        t.setheading(90)
        t.fd(5)
        t.setheading(0)



draw_tree()
window.exitonclick()