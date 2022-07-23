user_input = input('Enter a number of stars: ')
user_int = int(user_input)

for var_range in range (user_int + 1):
    print("*" * var_range)