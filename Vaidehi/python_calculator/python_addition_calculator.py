#assign string input to number_one variable
number_one_str = input("Enter number one: ")
#change number_one variable to num1 integer variable
num1_int =  int(number_one_str)

#assign string input to number_two variable
number_two_str = input("Enter number two: ")
#change number_two variable to num2 integer variable
num2_int = int(number_two_str)

#assigning number_one and number_two variables to answer
answer = num1_int + num2_int
#change answer to string data type to match other data types
#remember to change all lines to the same data type!
string = str(answer)
#put all pieces together using string data type and assign to variable
final_answer = number_one_str + " + " + number_two_str + " = " + string
print (final_answer)

