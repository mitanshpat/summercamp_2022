months_of_the_year = ["January", "February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("Months with 31 days: ")
for x in range(0,12):
    if x == 0 or x == 2 or x ==6 or x == 7 or x == 9 or x == 11:
        print(months_of_the_year[x])