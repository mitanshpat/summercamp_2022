user_input = input("Enter something: ")
user_input = user_input.strip()

if user_input.isnumeric():
    print("Your input is a number.")
else:
    print("Your input is letters.")