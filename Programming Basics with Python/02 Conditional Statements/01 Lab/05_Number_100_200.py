chosen_number = int(input())

if chosen_number < 100:
    print('Less than 100')
elif 100 <= chosen_number <= 200:
    print('Between 100 and 200')
else:
    print('Greater than 200')