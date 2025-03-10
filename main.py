from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
  question_text=question["question"]
  question_answer=question["correct_answer"]
  new_question=Question(question_text,question_answer)
  question_bank.append(new_question)
  
quiz_brain=QuizBrain(question_bank)
  
def main(): 
  if quiz_brain.still_has_questions():
    quiz_brain.next_question()
    main()
  else:
    print("Quiz Complete!")
    print(f"Your score is {quiz_brain.score}/{quiz_brain.question_count}")
      
main()