user_input = input('Enter a name of fruit: ').capitalize()

thislist = []

while user_input != 'Quit':
    thislist.append(user_input)
    user_input = input('Enter a name of fruit: ').capitalize()
print(thislist)
