name_i = input("enter a name: ")
removed_letter = input("enter the letter you want to remove: ")

look_for_r_l = name_i.find(removed_letter)

if look_for_r_l != -1:
    strip_v = name_i.replace(removed_letter, "")
    print(strip_v)
else:
    print("the letter " + removed_letter + " is not in " + name_i + ".")
