from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question['text']
    answer = question['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

new_question = QuizBrain(question_bank)
while new_question.still_has_questions():
    new_question.next_question()

print("You have completed the quiz")  
print(f"your final score is: {new_question.score}/{new_question.question_number}")  
    
    
