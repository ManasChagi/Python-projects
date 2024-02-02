from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

qbank = []
for each in question_data:
    question_text = each["question"]
    question_answer = each["correct_answer"]
    newq = Question(question_text, question_answer)
    qbank.append(newq)

quiz = Quizbrain(qbank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed your quiz")
print(f"your final score is {quiz.score}/{quiz.qno}")

