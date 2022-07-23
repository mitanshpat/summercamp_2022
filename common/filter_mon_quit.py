user_input = (input('Enter a string: ')).lower()
month_of_year = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
is_ = True

while user_input != "quit":
 y = True
 for x in month_of_year:
    find_x = x.find(user_input)
    if find_x != -1:
        y = False
        print(x.capitalize())
 if y == True:
        print('There are no months that match your input.')
 user_input = (input('Enter a string: ')).lower()



