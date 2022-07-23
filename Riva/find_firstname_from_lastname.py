name_bank = {
    "Riva": "Patel",
    "Vaidehi": "Bhagat",
    "Risha": "Patel",
    "Yani": "Bhagat",
    "Mitaansh": "Patel",
    "Vaishali": "Desai",
    "Anjana": "Desai",
    "Suhaan": "Shah",
    "Sana": "Shah",
}

user_i = input("Insert a name: ")

list_of_name_bank = name_bank.keys()
#print(list_of_name_bank)

for x in list_of_name_bank:
    if name_bank.get(x) == user_i:
        print(x)
    else:
        continue
