months_of_the_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
'''
for x in range (0,12):
    print(months_of_the_year[x] + " " + str(x))
'''

for x in range (0,12):
    if x == 0 or x==2 or x==4 or x==6 or x==7 or x==9 or x==11:
        print(months_of_the_year[x])