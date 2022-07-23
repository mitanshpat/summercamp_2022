import operator


number_1 = int(input("Enter first number: "))
operator_v = input("Enter operator: ")
number_2 = int(input("Enter second number: "))

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

display_number = ops[operator_v](number_1,number_2)
print(display_number)