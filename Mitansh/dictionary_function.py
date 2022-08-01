thisdict = {
    'Me' :'Mitansh Patel',
    'Bother' :'Jenil Patel',
    'Mother' :'Vanita Patel',
    "Father" :'Nilesh Patel'
}
user_input = input('Enter a family member: ').lower().capitalize()

while user_input != "quit":
    if thisdict.get(user_input) != None:
        print(thisdict.get(user_input))
    else:
        quit()
    print(thisdict.update())
    user_input = input('Enter a family member: ').lower().capitalize()
