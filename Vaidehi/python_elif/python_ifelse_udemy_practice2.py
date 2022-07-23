user_input = input("Enter your total marks in school (0 - 100 marks): ")
marks = int(user_input)

#we need to check whether the user input is valid before evaluating the program

if marks>100 or marks<0:
    print("Please enter a valid input (0-100) and run the program again.")
    quit()
if marks>=95 and marks<=100:
    print("Excellent!")
elif marks>=75 and marks<=95:
    print("Very good!")
elif marks>=55 and marks<=74:
    print("Satisfactory")
else:
    print("You need to work harder")

