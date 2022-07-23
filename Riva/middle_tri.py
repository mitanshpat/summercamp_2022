user_input = int(input("enter number here:"))

if user_input%2 != 0:
    v_outer = int(user_input/2) +1

else:
    v_outer = int(user_input/2)

for x in range (1, v_outer+1):
    print()