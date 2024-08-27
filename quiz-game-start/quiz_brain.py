class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.user_score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.user_score}/{self.question_num}\n")

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_guess = input(f"Q.{self.question_num}: {current_question.question} (True / False): ")
        self.check_answer(user_guess, current_question.answer)

