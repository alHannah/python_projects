from turtle import *

hannah = Turtle()
screen = Screen()

hannah.shape("turtle")
print(hannah)
print(screen)
screen.bgcolor("navy blue")
hannah.color("cyan")
hannah.forward(100)
hannah.backward(200)
screen.exitonclick()

# from prettytable import *
#
# table = PrettyTable()
# table.add_column("Name", ["Al Hannah", "James", "Peter", "Sarah"])
# table.add_column("Sex", ["Female", "Male", "Male", "Female"])
# table.align = "l"
# print(table)