from turtle import Turtle

import random

    
CROSSER_SHAPE = "turtle"
class CrossingTurtle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape(CROSSER_SHAPE)
        self.penup()
        self.goto(x= 0,
                  y= -280)
        self.setheading(90)  
                  
    def reset(self):
        self.goto(x= 0,
                  y= -280)
        
    def move_crosser_fd(self):
        self.fd(10)
        
    def move_crosser_bk(self):
        self.bk(10)
        

CARD_SHAPE = "square"
CARD_COLOR = ["red", "cyan", "blue", "purple", "yellow", "green"]
class Card:
    
    def __init__(self):
        self.card_generated = []
        
    def make_card(self):
        appear_car = random.randint(1, 6)
        if appear_car == 1:
            make_turtle = Turtle("square")
            make_turtle.color(random.choice(CARD_COLOR))
            make_turtle.turtlesize(stretch_wid= 1,
                                    stretch_len= 2)
            make_turtle.showturtle()
            make_turtle.penup()
            make_turtle.goto(x= 300,
                             y= random.randint(-240, 220))
            self.card_generated.append(make_turtle)
            
    def move_card(self):
        for card in self.card_generated:
            card.bk(random.randint(20, 40))


TEXT_COLOR = "black"
TEXT_ALIGN = "center"
TEXT_FONT = ("Courier", 24, "normal")
class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("/Users/hannah/ALLIN_PYTHON/Py/CROSSING_TURTLE/score_file.txt") as data:
            self.highest_score = data.read()
            if self.highest_score == '':
                self.highest_score = 0
            else:
                self.highest_score = int(self.highest_score)
        self.make_scoreboard()

    def make_scoreboard(self):
        self.clear()
        self.goto(x= -50,y= 270)
        self.write(f"High score: {self.highest_score} Score: {self.score}", align=TEXT_ALIGN, font=TEXT_FONT)

    def add_score(self):
        self.score += 1
        self.make_scoreboard()

    def game_over(self):
        self.goto(x= 0,y= 0)
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open(file= "/Users/hannah/ALLIN_PYTHON/Py/CROSSING_TURTLE/score_file.txt", mode= "w") as file:
                file.write(str(self.highest_score))
        self.write("GAME OVER", align=TEXT_ALIGN, font=TEXT_FONT)
