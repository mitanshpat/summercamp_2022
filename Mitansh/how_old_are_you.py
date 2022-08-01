user_input = input('Enter date of birth: ')

from datetime import datetime
str_d1 = user_input

d1 = datetime.strptime(str_d1, "%Y/%m/%d")


#delta = d2 - d1
delta = datetime.now() - d1
years = delta.days // 365
print('Difference is '+str(delta.days)+' days')
print('Difference is '+str(years)+' years')
print('Difference is '+str( years *12)+' months')



