#getting user input and storing string data type
user_input1 = input("Enter first number: ")

#creating a integer variable for converting user_input 1 from string into integer
numb1 = int(user_input1)

#getting second user input and storing string data type
user_input2 = input("Enter a second number: ")

# creating a integer variable for converting user_input 2 from string into integer
numb2 = int(user_input2)

#creating a integer variable for adding user input one + two
answer = numb1 + numb2

#converting answer from integer to string variable
answer = str(answer)


# creating a string variable to add the user_input1 and user_input2
s_answer = (user_input1 + ' + ' + user_input2 + ' = '+ answer )

#printing
print(s_answer)


# You can't add a integer and a string together