user_input = input("Enter a number: ")
print(type(user_input))
user_input_int = int(user_input)
print(type(user_input_int))

#value of mul_range always going to be 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
for mul_range in range(1,11):
  #user_input_int is 4
  #dislplay_text = 4 times 1
  #display_text = 4
    display_text = user_input_int*mul_range
    print(user_input + " x " + str(mul_range) + " = " + str(display_text))


