for i in range(1,100): 
    if(i%3==0):
        print("Bizz")
        if(i%5 == 0):
            print("BizzBuzz")
    elif(i%5==0):
        print("Buzz")
    
    else:
        print(i)