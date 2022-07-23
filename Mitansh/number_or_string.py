user_input = input('Enter anything: ')
user_input = user_input.strip()

if user_input.isnumeric() :
    print('it is a number')
else:
    print('is string')