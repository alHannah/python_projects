from data import *
from question_model import *
from quiz_brain import *

game = True
question_bank = []
for every_question in question_data:
    text = every_question['question']
    answer = every_question['correct_answer']
    question = Question(text, answer)
    question_bank.append(question)

q_brain = QuizBrain(question_bank)

while q_brain.still_has_question():
    q_brain.next_question()

score = q_brain.score
q_number = q_brain.question_number
print("Congratulations! You finished the Quiz")
print(f"Your final Score was: {score}/{q_number}")
