import time

user_input = int(input("Please enter a number: "))

for range_v in range(1,user_input + 1):
    print("*" * range_v)
    time.sleep(0.6)
