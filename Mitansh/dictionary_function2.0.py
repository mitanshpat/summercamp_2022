empty_dict = dict()
user_input_key = input('Enter a key: \n').capitalize()
if user_input_key == 'Quit':
    print(empty_dict)
    quit()
user_input_value = input('Enter the value to the key: \n').capitalize()


while user_input_key.capitalize()  != 'Quit':
    empty_dict.update({user_input_key: user_input_value})
    user_input_key = input('Enter a key: \n')
    if user_input_key == 'Quit':
        break
    user_input_value = input('Enter the value to the key: \n')
    empty_dict.update({user_input_key : user_input_value})

print(empty_dict)