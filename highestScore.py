student_score = input("Enter the score of students seperated by spaces.\n").split(" ")

highehst_score = 0

for i in range(0, len(student_score)):
    student_score[i] = int(student_score[i])
    if student_score[i] > highehst_score:
        highehst_score = student_score[i]

print(f"The highest score in the class is: {highehst_score}") 

