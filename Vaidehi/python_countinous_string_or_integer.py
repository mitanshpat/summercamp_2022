user_input = input("Enter something: ")
numeric = user_input.isnumeric()

while user_input != "quit":
    if numeric == True:
        print(user_input + " is a number.")
    else:
        print(user_input + " is a string.")
    user_input = input("Enter something: ")
print("Thank you for chatting with me!")
