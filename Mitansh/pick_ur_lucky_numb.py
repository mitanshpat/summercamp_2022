user_input = input("Enter your lucky number: ")
lucky_number = int(user_input)

i = 0
while i<= 100:
    if lucky_number == i:
        print (str(i) +": " +' This is your lucky number')
    else:
        print(i)
    i = i + 1




