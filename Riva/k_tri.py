user_input = int(input("Please enter a number: "))
user_input_c = user_input


while user_input_c != 0:
    print("*" * user_input_c)
    user_input_c = user_input_c - 1

for range_v in range(1, user_input + 1):
    print("*" * range_v)