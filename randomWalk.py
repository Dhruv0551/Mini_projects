from turtle import Turtle, Screen
import random

colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "black", 
"gray", "brown", "cyan", "magenta", "lime", "navy", "teal", "gold", "silver", 
"pink", "violet", "turquoise", "maroon", "beige", "salmon", "coral", "indigo", 
"chocolate", "lavender"

]

timmy = Turtle()
timmy.speed("fastest")
timmy.pensize(15)
directions = [timmy.left,timmy.right]

timmy.shape('turtle')


def randomwalk(direction):
	timmy.pencolor(random.choice(colors))
	timmy.forward(30 )
	direction(90)


for _ in range(300):
	direction = random.choice(directions)
	randomwalk(direction)

screen = Screen()
screen.exitonclick()
