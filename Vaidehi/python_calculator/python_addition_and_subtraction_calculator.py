#assign string input to number_one variable
number_one = input("Enter number one: ")
#change number_one variable to num1 integer variable
num1 = int(number_one)

operant = input("Enter operant: ")
#operant1 = int(operant)


#assign string input to number_two variable
number_two = input("Enter number two: ")
#change number_two variable to num2 integer variable
num2 = int(number_two)

#create variable to add num1 and num2
addition = num1 + num2
#create variable to change addition variable to string data type
plus = str(addition)
#create a variable to subtract num1 and num2
subtraction = num1 - num2
#create variable to change subtraction variable to string data type
minus = str(subtraction)

if operant == '+':
    print (number_one + " + " + number_two + " = " + plus)
else:
    print (number_one + " - " + number_two + " = " + minus)
