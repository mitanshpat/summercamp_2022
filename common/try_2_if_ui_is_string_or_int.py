user_input = (input("Enter something: ")).strip().lower()
#user_input = user_input.lower()|

while user_input != "quit":
  u_i_isnumeric = user_input.isnumeric()
  if u_i_isnumeric == True:
      print(user_input + " is a number.")
  else:
      print(user_input + " is a string.")
  user_input = (input("Enter something: ")).strip()
  user_input = user_input.lower()

print("Thanks for running this code.")