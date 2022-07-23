# creating a user input variable to get user input
user_input = input('Enter your name: ')

first_name = 'Mitansh'
last_name1 = ' Patel '
age_1 =  14
age_1_str = str(age_1 )

second_name = 'Riva'
last_name1 = ' Patel '
age_1 =  14
age_1_str = str(age_1 )

third_name = 'Vaidehi'
last_name2 = ' Bhagat '
age_2 = 15
age_2_str = str(age_2 )


if user_input == first_name:
    print(first_name + last_name1 + age_1_str + ' years old')
elif user_input == second_name:
    print(second_name + last_name1 + age_1_str + ' years old')
elif user_input == third_name:
    print(third_name + last_name2 + age_2_str + ' years old')


