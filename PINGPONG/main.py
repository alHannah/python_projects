from turtle import Screen
from pong import Pong, Paddle, Score

import time

screen = Screen()
screen.title('Ping Pong')
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


paddle_1 = Paddle()
paddle_2 = Paddle()
score = Score()
pong = Pong()

paddle_1.paddle_position(350, 0)
paddle_2.paddle_position(-350, 0)
right_side = 320
left_side = -320

screen.listen()
screen.onkey(paddle_1.paddle_up, "Up")
screen.onkey(paddle_1.paddle_down, "Down")
screen.onkey(paddle_2.paddle_up, "w")
screen.onkey(paddle_2.paddle_down, "s")

# Main game loop
game_active = True
while game_active:
    screen.update()
    pong.pong_move()
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.pong_bounce_y()
    if pong.xcor() > right_side and pong.distance(paddle_1) < 50:
        pong.pong_bounce_x()
    elif pong.xcor() > 380:
        pong.pong_bounce_x()
        score.add_l_score()
        
    if pong.xcor() < left_side and pong.distance(paddle_2) < 50:
        pong.pong_bounce_x()
    elif pong.xcor() < -380:
        pong.pong_bounce_x()
        score.add_r_score()
    
    time.sleep(0.1)
    
screen.exitonclick()
