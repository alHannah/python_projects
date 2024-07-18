from turtle import Turtle
TURTLE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

TURTLE_SHAPE= 'square'
TURTLE_COLOR = 'green'
BORDER_COLOR = 'green'


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.show_snake()
        self.snake_head = self.snake_body[0]
        self.make_border()

    def show_snake(self):
        for make_body in TURTLE_POSITION:
            self.make_snake(make_body)

    def make_snake(self, snake_position):
        new_turtle = Turtle(TURTLE_SHAPE)
        new_turtle.color(TURTLE_COLOR)
        new_turtle.penup()
        new_turtle.goto(snake_position)
        self.snake_body.append(new_turtle)

    def grow_snake(self):
        self.make_snake(self.snake_body[-1].position())

    def move(self):
        for every_body in range(len(self.snake_body) - 1, 0, - 1):  # This range has start, stop, step like in C
            new_x = self.snake_body[every_body - 1].xcor()  # To assign a new coordinate from previous
            new_y = self.snake_body[every_body - 1].ycor()  # To assign a new coordinate from previous
            self.snake_body[every_body].penup()
            self.snake_body[every_body].goto(new_x, new_y)  # every_body will be 2-1-0 step of -1 instead of 0-1-2
        self.snake_head.fd(DISTANCE)

    def make_border(self):
        self.penup()
        self.hideturtle()
        self.pencolor(BORDER_COLOR)
        self.goto(x=300, y=300)
        self.setheading(DOWN)
        self.pensize(10)
        self.pendown()
        self.fd(600)
        self.setheading(LEFT)
        self.fd(600)
        self.setheading(UP)
        self.fd(600)
        self.setheading(RIGHT)
        self.fd(600)

    def snake_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def snake_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def snake_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def snake_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

