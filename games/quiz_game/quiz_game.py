from data import question_data
from question_model import Question
from quiz_logic import QuizLogic

# The code is creating a list of Question objects. It iterates over the question_data list and for
# each question, it extracts the question text and correct answer. It then creates a new Question
# object using the extracted data and appends it to the questions list. Finally, it prints the list of
# Question objects.
questions = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

quiz = QuizLogic(questions)
quiz.next_question()