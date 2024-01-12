import turtle
import random

window = turtle.Screen()
window.setup(height=480, width=480)

race_start = False
user_bet = window.textinput(title="Turtle Race", prompt="Turtle: ").lower()

if user_bet:
    race_start = True

turtle_color = ["red", "cyan", "blue", "purple", "yellow", "green"]

turtles = []

# print(user_bet)

for shape in range(0, 6):
    new = turtle.Turtle(shape="turtle")
    turtles.append(new)

color = 0
for pet in turtles:
    pet.color(turtle_color[color])
    color += 1

print(turtles)


def position(coordinate_x, coordinate_y):
    for every_turtle in turtles:
        every_turtle.penup()
        every_turtle.goto(x=-coordinate_x, y=coordinate_y)
        coordinate_y -= 50


position(230, 90)

while race_start:
    distance = [(220, 90), (220, 40), (220, -10), (220, -60), (220, -110), (220, -160)]
    for every_move in turtles:
        every_move.speed("fastest")
        rand_move = random.randint(0, 10)
        every_move.fd(rand_move)
        if every_move.xcor() > 210:
            if user_bet in every_move.pencolor():
                print("you win!")
            else:
                print(f"you loose the winer is: {every_move.pencolor()}")
            race_start = False


window.exitonclick()
