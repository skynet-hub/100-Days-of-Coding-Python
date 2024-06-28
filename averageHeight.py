#seperate using space

student_height = input("Input a list of students height sepearted by space \n").split(" ")
count = 0
sum = 0

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
    sum += student_height[n]
    count += 1  #This cpould have easily been done using sum and len functions of lists but for emphasis of for loops I used this instead

average = round(sum / count)

print(student_height)
print(f"The average height of students in this class is: {average}")