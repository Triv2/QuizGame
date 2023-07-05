class QuizBrain:
  def __init__(self, list_of_questions):
    self.question_list = list_of_questions
    self.score=0
    self.question_count=0
  
  def get_question(self):
    question = self.question_list[self.question_count]
    if question:
      print(question)
    else:
      print("No question found.")
  
  def check_answer(self, user_answer, correct_answer):
    valid_user_answer = user_answer.lower()
    valid_correct_answer = correct_answer.lower()
    if valid_user_answer==valid_correct_answer:
      print("Correct!")
      self.score+=1
    else:
      print("Wrong!")
    print(f"The correct answer is {correct_answer}")
    print(f"Your score is {self.score}/{self.question_count}\n")
      
  def still_has_questions(self):
    length = len(self.question_list)
    if self.question_count < length:
      return True
    else:
      return False
  
  def next_question(self):
    current_question = self.question_list[self.question_count]
    self.question_count+=1
    user_answer = input(f"Q.{self.question_count}: {current_question.question} (True/False): ")
    self.check_answer(user_answer, current_question.answer)
    
    
  
  
  