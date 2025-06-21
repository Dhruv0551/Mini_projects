class QuizBrain:

	def __init__(self,q_list):
		self.q_number = 0
		self.points = 0
		self.q_list = q_list

	def stillHasQuestions(self):
		if self.q_number < len(self.q_list):
			return True
		else:
			print(f"Your Final Score is: ({self.points}/{self.q_number})")
			return False

	def nextQuestion(self):
		current_Question = self.q_list[self.q_number]
		self.q_number+=1
		user_answer = input(f"Q.{self.q_number}: {current_Question.question} (True/False): ")
		self.checkAnswer(user_answer,current_Question.answer)


	def checkAnswer(self,user_answer,correct_answer):
		if user_answer.lower() == correct_answer.lower():
			print("You got it right")
			self.points+=1	
		else:
			print("Incorrect Answer")
		print(f"Your Score is ({self.points}/{self.q_number})")
		print("\n"*2)