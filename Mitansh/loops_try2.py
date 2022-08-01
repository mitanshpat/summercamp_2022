user_input = input("Enter a number: ")
user_input = int(user_input)
for i in range (2,user_input+1):
    isPrime=True
    for j in range(2,int(i/2)+1):
            print('Number is prime')
