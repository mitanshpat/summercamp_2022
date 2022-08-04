#user_input_key = input('Enter a key: \n').capitalize()
#if user_input_key == 'Quit':
    #print(empty_dict)
    #quit()
#user_input_value = input('Enter the value to the key: \n').capitalize()
empty_dict = dict()
user_input_key = input('Enter a key: \n').capitalize()

while user_input_key.capitalize()  != 'Quit':
    user_input_value = input('Enter the value to the key: \n').capitalize()
    empty_dict.update({user_input_key: user_input_value})
    user_input_key = input('Enter a key: \n')
    #if user_input_key == 'Quit':
     #   break

print(empty_dict)