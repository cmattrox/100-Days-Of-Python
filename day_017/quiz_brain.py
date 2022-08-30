class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.correct_answers = 0
    
    def next_question(self):
        answer = input(f"Question #{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def still_has_question(self):
        if (self.question_number < len(self.question_list)):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if (user_answer.lower() == correct_answer.lower()):
            self.correct_answers += 1
            print("That is correct!")
        else:
            print("That is not correct.")

        print(f"The correct answer was: {self.question_list[self.question_number].answer}\nYour current score is: {self.correct_answers}/{self.question_number + 1}\n")