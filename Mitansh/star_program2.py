#create a variable to get a user input
user_input = input('Enter a number of stars: ')
#convert user_input string from string to integer
user_int = int(user_input)

while  user_int != 0:
    print('*' * user_int)
    user_int = user_int - 1
