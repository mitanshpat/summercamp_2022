user_input = int(input("Enter number of rows: "))

constant = 0

for range_v in range(1, user_input + 1):
    for space in range(1, (user_input - range_v) + 1):
        print(end="  ")

    while constant != (2 * range_v - 1):
        print("* ", end=" ")
        constant += 1

    constant = 0
    print()