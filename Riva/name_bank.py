name_bank = {
    "Riva": "Patel",
    "Vaidehi": "Bhagat",
    "Risha": "is dumb",
    "Vaishali": "Desai",
}

user_i = input("Insert a name: ")

#print(user_i)

''''
if user_i != "riva":
    print("This is not a valid name.")
    quit()
    
elif user_i != "vaidehi":
    print("This is not a valid name.")
    quit()
elif user_i != "risha":
    print("This is not a valid name.")
    quit()
elif user_i != "vaishali":
    print("This is not a valid name.")
    quit()
'''
display_v = name_bank.get(user_i)
print(display_v)


