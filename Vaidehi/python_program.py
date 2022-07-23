user_input1 = input("Enter string one: ")
user_input2 = input("Enter string one: ")
after_strip1 = user_input1.strip()
after_strip2 = user_input2.strip()

if after_strip1.upper() == after_strip2.upper():
    print("Your strings are the same.")
else:
    print("Your strings are not the same.")