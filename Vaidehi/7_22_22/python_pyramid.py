user_input =int(input("Please enter row number: "))



if user_input%2 != 0:
    v_outer = int(user_input/2) + 1
else:
    v_outer = int(user_input/2)

for x in range (1, v_outer+1):
    print(user_input + 1 * "*")