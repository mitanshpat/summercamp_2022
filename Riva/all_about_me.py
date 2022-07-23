def shortend(vairable):
    return "Please enter your " + vairable
name_i = input(shortend("name: "))
place_i = input(shortend("favorite place to be: "))
color_i = input(shortend("favorite color: "))
animal_i = input(shortend("animal: "))

def all_abt_u(name, place, color, animal):
    return ("Your name is " +  name + ". " +
            "Your favorite place to be is " + place + ". " +
            "Your favorite color is " + color + ". " +
            "Your favorite animal is " + animal + ". ")
test = all_abt_u(name_i, place_i, color_i, animal_i)
print(test)


