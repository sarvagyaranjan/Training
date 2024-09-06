weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))

BMI = round(weight/((height)**2),2)
print("Your BMI is: ", BMI)

if(BMI<18.5):
    print("Underweight")
    
elif(BMI>=18.5 and BMI <25):
    print("Normal Weight")

elif(BMI>=25 and BMI<30):
    print("Overweight")

elif(BMI>=30 and BMI<35):
    print("Obese")

else:
    print("Clinically Obese")