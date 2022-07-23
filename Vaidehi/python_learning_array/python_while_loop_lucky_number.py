i = 0
lucky_number = input("Pick your lucky number: ")
lnumber = int(lucky_number)



while i<=10:
    if lnumber == i:
        print (str(i) + ":" + " this is your lucky number")
    else:
        print (i)
    i = i + 1
