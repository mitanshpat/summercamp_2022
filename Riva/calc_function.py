def calc(number_1,operator_v, number_2):
    import operator


    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

    display_number = ops[operator_v](number_1, number_2)
    display_number = str(number_1) + " " + operator_v + " " + str(number_2) + " = " + str(display_number)
    return display_number

output = calc(3, "*", 5)
print(output)