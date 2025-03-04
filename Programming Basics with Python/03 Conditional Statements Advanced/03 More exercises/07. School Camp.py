vacation = input().lower() # Winter, Spring or Summer;
group_type = input().lower() # boys, girls, mixed
number_students = int(input())
number_nights = int(input())

sport = ''

if group_type == 'boys' or group_type == 'girls':
    if vacation == 'winter':
        price_per_night = 9.6
    elif vacation == 'spring':
        price_per_night = 7.2
    elif vacation == 'summer':
        price_per_night = 15
elif group_type == 'mixed':
    if vacation == 'winter':
        price_per_night = 10
    if vacation == 'spring':
        price_per_night = 9.5
    elif vacation == 'summer':
        price_per_night = 20

vacation_cost = number_students * number_nights * price_per_night

if number_students >= 50:
    vacation_cost = 0.5 * vacation_cost
elif 20 <= number_students < 50:
    vacation_cost = (1 - 0.15) * vacation_cost
elif 10 <= number_students < 20:
    vacation_cost = (1 - 0.05) * vacation_cost

if vacation == 'winter':
    if group_type == 'girls':
        sport = 'gymnastics'
    elif group_type == 'boys':
        sport = 'Judo'
    else:
        sport = 'ski'
elif vacation == 'spring':
    if group_type == 'girls':
        sport = 'athletics'
    elif group_type == 'boys':
        sport = 'Tennis'
    else:
        sport = 'cycling'
elif vacation == 'summer':
    if group_type == 'girls':
        sport = 'volleyball'
    elif group_type == 'boys':
        sport = 'football'
    elif group_type == 'mixed':
        sport = 'Swimming'

print(f'{sport.capitalize()} {vacation_cost:.2f} lv.')