user_input = input('insert number: ')
number_one = int(user_input)
user_input= input('enter number 2: ')
number_two = int(user_input)
number_one = str(number_one)
number_two = str(number_two)
if number_one > number_two:
  print(number_one + " is greater than " + number_two )
else:
  print(number_one + " is less than " + number_two)