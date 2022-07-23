string_1 = input("Enter your first string: ")
string_2 = input("Enter your second string: ")

formated_string_1 = string_1.lower()
formated_string_2 = string_2.lower()

formated_string_1 = string_1.strip()
formated_string_2 = string_2.strip()

if formated_string_1 == formated_string_2:
    print("They are same.")
else:
    print("They are different.")


