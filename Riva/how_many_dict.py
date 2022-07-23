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

tuple_v = tuple(list_of_name_bank)

list_v = list(name_bank.values())
#print(list_v)

x = list_v.count(user_i)
print(x)

#print(list_of_name_bank)

#x = list_of_name_bank.count()
#print(x)
