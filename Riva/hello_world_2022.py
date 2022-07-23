user_input = input("Type a number")
user_input_num = int(user_input)
print(user_input_num)
result = user_input_num*3
print(result)

your_list = [10,20,30,40,50,60,70,80,90]
new_list = [x / 10 for item in your_list]

print(new_list)