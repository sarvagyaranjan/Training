height = int(input("Enter your height: "))


if height>=120:
    
    print("Can ride")
    age = int(input("Enter your age: "))
    if(age<12):
        print("Rs. 50")
    elif(12<age<18):
        print("Rs. 100")
    else:
        print("Rs. 150")


else: 
    print("Can't ride")