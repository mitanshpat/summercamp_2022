count = 0

for x in range(1,10000):
    if x%35 == 0:
        count = count+1
        print(x)
print("Total number of quotiants printed: " + str(count))