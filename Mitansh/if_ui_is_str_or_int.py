#variable for user input: string
user_input = input('Enter anything: ')
#sample user_input: " 123"
#u_i_strip will be "123"
u_i_strip = user_input.strip()

#sample user_input: " 123"
#u_i_strip is "123"
while u_i_strip != 'quit':
    #it will go inside the if
    if u_i_strip.isnumeric():
        #it will print "it is numeric"
        print("it is numeric.")
        #user_input is " 345"
        user_input = input('Enter anything: ')
    else:
        print(user_input)
        user_input = input('Enter anything: ')
print('Thanks for chatting with me')