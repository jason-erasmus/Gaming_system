class QuizLogic:

    def __init__(self,q_list):
        self.question_num = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        input(f"Q.{self.question_num}: {current_question.text} (True/False): ")

    def still_question(self):
        current_question > len(self.question_list)
        