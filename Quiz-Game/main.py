from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

q_list = []

for question in question_data:
	text_question = question["text"]
	text_answer = question["answer"]
	new_q = Question(text_question,text_answer)
	q_list.append(new_q)


quiz = QuizBrain(q_list)
quiz.nextQuestion()