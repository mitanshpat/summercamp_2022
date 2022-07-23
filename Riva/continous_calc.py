import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


number = int(input("Enter a number: "))
operator_v = input("Enter operator: ")
number_1 = int(input("Enter a number: "))

display_text = ops[operator_v](number, number_1)
operator_v = input("Enter operator: ")

while operator_v != "=":
    display_text = ops[operator_v](display_text, number_1)
    number_1 = int(input("Enter number: "))
    operator_2 =  input("Enter operator: ")
    if operator != "=":
        operator_v = operator_2
        continue
    else:
        display_text = ops[operator_v](display_text, number_1)
        break

print(display_text)








'''    
    operator_v = input("Enter operator : ")
    if operator_v != "=":
        if operator_v == "=":
            number_1 = int(input("Enter a number: "))
            display_text = ops[operator_v](display_text, number_1)
            operator_v = input("Enter operator : ")
            number_1 = int(input("Enter a number: "))
        else:
         if operator_v == "=":
            display_text = ops[operator_v](display_text, number_1)
            break
    else:
        break

        #break
    #else:
        #operator_v == operator_2
        #display_text = ops[operator_v](number_1, display_text)


print(display_text)
'''