from turtle import Screen
import time
from snake import Snake
from scoreboard import ScoreBoard
from food import Food

# window
window = Screen()
# Game window setup
window.title("My Snake Game")
window.screensize(600,
                  600,
                  "white")
window.tracer(0)

# snake
snake = Snake()
# Food
food = Food()
# Words and border
words = ScoreBoard()

# Snake Level (Snake speed)
difficulty = window.textinput("DIFFICULTY",
                              "Easy (e), Medium (m), Hard (h)").lower()
snake_speed = 0
if difficulty == 'e':
    snake_speed = 0.1
    in_game = True
elif difficulty == 'm':
    snake_speed = 0.05
    in_game = True
elif difficulty == 'h':
    snake_speed = 0.01
    in_game = True
else:
    in_game = False


# Snake Moves
window.listen()
window.onkey(snake.snake_up, "Up")
window.onkey(snake.snake_down, "Down")
window.onkey(snake.snake_left, "Left")
window.onkey(snake.snake_right, "Right")

# Snake Logic
while in_game:
    window.update()
    time.sleep(snake_speed)  # it depends from difficulty
    snake.move()  # Make snake move
    # words_border.make_border()  # Show game border

    # detect if snake eat food
    if snake.snake_head.distance(food) < 15:
        # print("gulp")  # testbench if food is detected
        food.refresh()  # random food generator depends on screen size
        snake.grow_snake()  # Make snake longer
        words.add_score()  # Score monitoring

    # detect if snake touch the screen border
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        in_game = False
        words.dead()

    # detect if snake eat his body
    for body_parts in snake.snake_body:
        if body_parts == snake.snake_head:
            pass
        elif snake.snake_head.distance(body_parts) < 10:
            in_game = False
            words.dead()


window.exitonclick()
