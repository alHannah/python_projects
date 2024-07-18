from turtle import Turtle
import random

FOOD_COLOR = 'red'
FOOD_SHAPE = 'circle'


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5,
                       stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(a=-270,
                                b=270)
        rand_y = random.randint(a=-270,
                                b=270)
        self.goto(rand_x, rand_y)


