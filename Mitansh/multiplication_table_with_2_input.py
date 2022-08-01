user_input = input('Enter table starting number: ')
user_input_2 = input('Enter table and number: ')

#creating variable called u_i_str to convert user_input from string to integer
u_i_int = int(user_input)
u_i_2_int = int(user_input_2)



#if table is four and you need to print till 20
#u_i_int will be 4
#u_i_2_int will be 20
#for v_range in range (1, 20)
#v_range would be 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...20

for v_range in range (1, u_i_2_int + 1, 2 ):
#when v_range is 1 #answer = 4*1 #answer = 4
#when v_range is 2 #answer = 4*2 #answer = 8
    answer = u_i_int * v_range
    #  4 x 1 = 4
    print(user_input + ' x ' + str(v_range) + ' = ' + str(answer))