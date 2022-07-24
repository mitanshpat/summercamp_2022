user_input = input('Enter anything: ')

while user_input != 'quit':
    if user_input.isnumeric():
        print('It is a integer')
        user_input = input('Enter anything: ')
    else:
        print('It is a string')
        user_input = input('Enter anything: ')
print('Thanks for chatting with me')