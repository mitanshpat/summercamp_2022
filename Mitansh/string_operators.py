
user_input = input('Enter a name: ')
u_input2 = input('Enter the same name in upper case: ')
user_input = user_input.upper()
u_input2 = u_input2.upper()


if user_input.strip() == u_input2.strip():
    print('True')
else:
    print('False')