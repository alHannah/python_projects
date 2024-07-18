import turtle


snake = turtle.Turtle()
window = turtle.Screen()

window.screensize(canvwidth=400, canvheight=400)
snake.shape("turtle")
snake.color("Green")

snake.penup()
snake.goto(x=200, y=200)
snake.setheading(180)

window.exitonclick()