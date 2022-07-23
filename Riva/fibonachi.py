u_i=input('Enter a number: ')
u_i=int(u_i)

if u_i == 1:
  print("0")
  quit()
elif u_i == 2:
  print("0")
  print("1")
  quit()



fibo1=int(0)
fibo2=int(1)


print(fibo1)
print(fibo2)

x=u_i-2

for x in range (0,u_i-2):
  x=(fibo1+fibo2)
  print(x)
  fibo1=fibo2
  fibo2=x