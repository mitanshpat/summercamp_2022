user_input = input("Enter something: ")
u_i_strip = user_input.strip()

while user_input.lower() != "quit":
    if u_i_strip.isnumeric() == True:
        print(user_input + " is a number.")
    else:
        print(user_input + " is a string.")
    user_input = input("Enter something: ")
print("Thank you for chatting with me!")
