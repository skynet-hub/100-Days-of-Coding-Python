#BMI calculator

print("Welcoe to the BMI calculator")

#Get user info

height = float(input("What is your height in meters\n"))
weight = float(input("Enter your wieght in kgs\n"))

#compute BMI
BMI = weight / height ** 2
final_BMI = round(BMI)

#print out the result

if final_BMI < 18.5:
    print(f"Your BMI is: {final_BMI}, you are underweight...")
elif final_BMI >= 18.5 and final_BMI < 25:
    print(f"Your BMI is: {final_BMI}, you are normal weight.")
elif final_BMI >= 25 and final_BMI < 30:
    print(f"Your BMI is: {final_BMI}, you are overwight..")
elif final_BMI >= 30 and final_BMI < 35:
    print(f"Your BMI is: {final_BMI}, you are obese.")
else:
    print(f"Your BMI is: {final_BMI}, you are clinically obese.")                