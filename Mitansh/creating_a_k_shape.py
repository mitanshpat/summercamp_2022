'''user_input = input('Enter the number of stars: ')

user_int = int(user_input)

user_input2 = user_int

while user_input2 !=0:
    print('*'* user_input2)
    user_input2 = user_input2 - 1
for var_range in range (user_int + 1):
    print('*'* var_range)'''

user_input = input ('Enter the number of stars:  ')

user_int = int(user_input)

for a in range (1,user_int +1):
    for b in range (a, user_int + 1):
        print ('*', end="")
    print('')


