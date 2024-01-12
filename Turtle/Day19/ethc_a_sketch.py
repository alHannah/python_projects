import turtle

fin = turtle.Turtle()
window = turtle.Screen()
fin.speed("fastest")


def run():
    fin.fd(5)

def backwards():
    fin.bk(5)

def turn_l():
    fin.setheading(fin.heading() + 5)

def turn_r():
    fin.setheading(fin.heading() - 5)

def clear():
    fin.reset()


window.listen()
window.onkey(fun = run, key = "w")
window.onkey(backwards, "s")
window.onkey(turn_l, "a")
window.onkey(turn_r, "d")
window.onkey(clear, "c")
window.exitonclick()
