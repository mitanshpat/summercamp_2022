def isprime(user_input):
 user_input = int((user_input))
 if user_input == 1:
    return False

 if user_input == 2:
    return True

 user_input_divided_2 = user_input%2
 if user_input_divided_2 == 0:
    return False
 else:
    half = int(user_input/2)
    for x in range(3,half):
        v_stuff = user_input%x
        if v_stuff == 0:
            return False

 return True



trial = isprime(59)
print(trial)







