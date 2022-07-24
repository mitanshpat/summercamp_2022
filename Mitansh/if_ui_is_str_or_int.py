#variable for user input: string
user_input = input('Enter anything: ').strip().lower()
#sample user_input: " 123"
#u_i_strip will be "123"
#u_i_strip = user_input.strip()
#user_input = user_input.lower()
#sample user_input: " 123"
#u_i_strip is "123"
while user_input != 'quit':
    #it will go inside the if

    if user_input.isnumeric() == True:
        #it will print "it is numeric"
        print("it is numeric:"+user_input)
        #user_input is " 345"

    else:
        print('Your input is a string:'+user_input)
    user_input = input('Enter anything: ').strip().lower()

print('Thanks for chatting with me')