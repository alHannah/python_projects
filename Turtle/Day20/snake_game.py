import turtle

fin = turtle.Turtle()
window = turtle.Screen()

window.setup(width=600, height=600)
window.title("SNAKE GAME")
window.bgcolor("black")

# color = ["red", "blue", "green"]
x = 0
turtle_index = 0
body_frame = []
for body in range(0, 3):
    new = turtle.Turtle(shape="square")
    body_frame.append(new)
    # body_frame[turtle_index].speed("fast")
    body_frame[turtle_index].color("white")
    body_frame[turtle_index].goto(x=x, y=0)
    turtle_index += 1
    x -= 21


window.exitonclick()
