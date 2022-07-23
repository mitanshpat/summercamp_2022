user_input = int(input("Enter a number: "))

for x in range(1, user_input + 1):
    for y in range(x, user_input+1):
        print("*", end="")
    print("")