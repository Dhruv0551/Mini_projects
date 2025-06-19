import random
lives = 0

def guessing(lives):
	print("I'm thinkin of a Number between 1 and 100")
	while True:
		if lives == 0:
			print("You Lose🥀🥀")
			break
		User_int = int(input("Guess the Number: "))
		if User_int == ans:
			print("You Guessed the Number🤓🤓")
			break
		elif User_int > ans:
			print("Too High")
			lives-=1
			print(f"You have {lives} lives Left")
		elif User_int < ans:
			print("Too Low")
			lives-=1
			print(f"You have {lives} lives Left")



def easy():
	guessing(10)

def hard():
	guessing(5)
	

ans = random.randint(1,100)
print("Welcome to the Guessing Game😁😁")
difficulty = input("Enter Difficulty You wanna Play in Easy or Hard(e/h): ")
if difficulty == "e":
	easy()
elif difficulty == "h":
	hard()
else:
	print("Invalid Input")