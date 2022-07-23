import time

user_input = input("Enter a number: ")
user_input_int = int(user_input)

for v_range in range (1, user_input_int + 1):
    print("*" * v_range)
    time.sleep(0.2)