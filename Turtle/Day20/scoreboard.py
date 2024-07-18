from turtle import Turtle

TEXT_ALIGN = "center"
TEXT_FONT = ("Courier", 24, "normal")
TEXT_COLOR = 'black'

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(TEXT_COLOR)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.make_scoreboard()

    def make_scoreboard(self):
        self.write(f"Score: {self.score}", align=TEXT_ALIGN, font=TEXT_FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.make_scoreboard()

    def dead(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", align=TEXT_ALIGN, font=TEXT_FONT)

