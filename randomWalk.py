from turtle import Turtle, Screen, colormode
import random

colormode(255)
angles = [0, 90, 180, 270]

def randomColor():
	r = random.randint(1,255)
	g = random.randint(1,255)
	b = random.randint(1,255)
	return (r,g,b)

timmy = Turtle()
timmy.speed("fastest")
timmy.pensize(15)
directions = [timmy.left,timmy.right]

timmy.shape('turtle')


def randomwalk(direction):
	timmy.pencolor(randomColor())
	timmy.setheading(direction)
	timmy.forward(30)


for _ in range(300):
	direction = random.choice(angles)
	randomwalk(direction)

screen = Screen()
screen.exitonclick()
