from datetime import datetime, timedelta

# strptime - convert string to datetime object
# strftime - convert datetime object to string

my_date = input('Enter a date: ')

# Use strptime to convert the input to datetime object
my_date = datetime.strptime(my_date, '%Y-%m-%d')

my_new_date = my_date + timedelta(days=1000)

print(my_new_date.strftime('%d-%m-%Y'))

