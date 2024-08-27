from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    new_question = item["text"]
    new_answer = item["answer"]
    add_question = Question(new_question, new_answer)
    question_bank.append(add_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.user_score}/{len(question_bank)}.")
