total_amount = float(input("Enter your total bill: "))
tip_percentage = float(input("Enter the tip percentage: "))

no_of_people = int(input("Enter number of people: "))

split = (total_amount/no_of_people)*(1+tip_percentage/100)

print("Each person should pay ", round(split,1))