
import datetime
import random

def get_birthdays(number_of_birthdays):
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001,1,1)
        random_number_of_days = datetime.timedelta(random.randint(0 , 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a , birthday_a in enumerate(birthdays):
        for birthday_b in birthdays[a + 1:]:
            if birthday_a == birthday_b:
                return birthday_a

MONTHS = ('Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun' , 
          'jul' , 'Aug' , 'Sep' , 'Oct' , 'Nov' , 'Dec')


while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break


print()

print('Here are ', num_bdays , 'birthdays:')
birthdays = get_birthdays(num_bdays)
for i , birthday in enumerate(birthdays):
    month_name = MONTHS[birthdays.month - 1]
    date_text = f'{month_name} , {birthday.day}'
    print(date_text , end='')
    if i <  num_bdays - 1 :
        print(', ' , end='')
print('\n')

match = get_match(birthdays)

print('In this simulation', end='')
if match:
    month_name = MONTHS[match.month - 1 ]
    date_text = f'{month_name} , {match.day}'
    print('multiply people have a birthday on ' , date_text)
else:
    print('there are no matching birthdays.')
print()

print("Generating" , num_bdays , ' random birthdays  100,000 times...')
input('press Enter to begin.....')

print('Let\'s run another 100,000 simulations. ')
sim_match = 0 
for i in range(100,000):
    if i % 10_000  == 0 :
        print(i , 'Simulations run ...')
    birthdays  = get_birthdays(num_bdays)
    if get_match(birthdays):
        sim_match += 1 
print('100,000 simulations run . ')

probability = round(sim_match / 100_000 * 100, 2)
print('Out of 100,000 simulations of', num_bdays, 'people, there was a')
print('matching birthday in that group', sim_match, 'times. This means')
print('that', num_bdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')





