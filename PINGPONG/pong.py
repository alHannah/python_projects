from turtle import Turtle


PONG_SHAPE = "circle"
PONG_COLOR = "white"
class Pong(Turtle):
    def __init__(self):
        super().__init__()
        # self.penup()
        self.shape(PONG_SHAPE)
        self.color(PONG_COLOR)
        self.move_x = 10
        self.move_y = 10
    
    def pong_move(self):
        position_x = self.xcor() + self.move_x
        position_y = self.ycor() + self.move_y
        
        self.goto(x= position_x,
                  y= position_y)
        
    def pong_bounce_x(self):
        self.move_x *= -1
        
    def pong_bounce_y(self):
        self.move_y *= -1
        


PADDLE_SPEED = 10
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(PADDLE_COLOR)
        self.shape(PADDLE_SHAPE)
        self.turtlesize(stretch_wid= 5,
                        stretch_len= 1)
        
    def paddle_position(self, position_x, position_y):
        self.setposition(x= position_x,
                         y= position_y)
        
    def paddle_up(self):
        ycor = self.ycor()
        ycor += PADDLE_SPEED
        self.sety(ycor)
        
    def paddle_down(self):
        ycor = self.ycor()
        ycor -= PADDLE_SPEED
        self.sety(ycor)
        


TEXT_COLOR = "white"
TEXT_ALIGN = "left"
TEXT_FONT = ("Courier", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.make_scoreboard()

    def make_scoreboard(self):
        self.clear()
        self.goto(-200, 270)
        self.write(f"Score: {self.l_score}", align=TEXT_ALIGN, font=TEXT_FONT)
        self.goto(200, 270)
        self.write(f"Score: {self.r_score}", align=TEXT_ALIGN, font=TEXT_FONT)

    def add_l_score(self):
        self.l_score += 1
        self.make_scoreboard()

    def add_r_score(self):
        self.r_score += 1
        self.make_scoreboard()
        