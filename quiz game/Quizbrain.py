class Quizbrain:
    def __init__(self, q_list):
        self.qno = 0
        self.qlist = q_list
        self.score = 0

    def still_has_questions(self):
        if self.qno < len(self.qlist):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.qlist[self.qno]
        self.qno += 1
        user_answer = input(f"Q.{self.qno}. {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("This is wrong answer")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is {self.score}/{self.qno}")
        print("\n")




