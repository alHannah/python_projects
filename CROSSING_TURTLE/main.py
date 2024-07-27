from turtle import Screen
from crossing_class import Card, CrossingTurtle, Text

import time

screen = Screen()
screen.title("CROSSING TURTLE")
screen.setup(width= 600,
             height= 600)
screen.bgcolor("white")
screen.tracer(0)


crosser = CrossingTurtle()
card = Card()
text = Text()

screen.listen()
screen.onkey(crosser.move_crosser_fd, "Up")
screen.onkey(crosser.move_crosser_bk, "Down")

turtle_is_running = True
while turtle_is_running:
    time.sleep(0.1)
    screen.update()
    card.make_card()
    card.move_card()
    
    for card_body in card.card_generated:
        if card_body.distance(crosser) < 20:
            text.game_over()
            turtle_is_running = False
    if crosser.ycor() > 280:
        text.add_score()
        crosser.reset()
    

screen.exitonclick()