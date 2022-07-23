user_input = input('Enter a number of lines: ')
user_int = int(user_input)

for x in range (user_int, 1, -1):
    for space  in range (0,user_int-x):
        print(' ', end= '')
    for y in range(x,2*x-1):
        print('*', end= '')
    for y in range(1, x-1):
        print('*', end= '')
    print()