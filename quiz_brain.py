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
  
  def get_answer(self):
    answer= self.question_list[self.question_count]
    if answer:
      print(answer)
    else:
      print("No answer found.")
    
  
  
  