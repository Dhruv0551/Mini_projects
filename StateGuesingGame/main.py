import turtle
import pandas as pd

screen = turtle.Screen()
data = pd.read_csv('50_states.csv')
screen.title("State Guessing Game")
state_image = "blank_states_img.gif"
screen.addshape(state_image)
turtle.shape(state_image)
score = 0
all_states = data.state.to_list()
guessed_states= []
while len(guessed_states) < 51:
	user_input = screen.textinput(title= f"Enter State({len(guessed_states)}/{len(data.state)})", prompt= "Write Name of Another State:").title()
	if user_input == "Exit":
		break
	if user_input in all_states and user_input not in guessed_states:
		guessed_states.append(user_input)
		state_data = data[data.state == user_input]
		x = int(state_data.x)
		y = int(state_data.y)
		markup = turtle.Turtle()
		markup.hideturtle()
		markup.penup()
		markup.goto(x,y)
		markup.write(user_input)

		
screen.mainloop()