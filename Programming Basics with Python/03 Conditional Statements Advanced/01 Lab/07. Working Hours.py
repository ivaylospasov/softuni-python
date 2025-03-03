hour = int(input())
day_of_week = input()

if day_of_week != 'Sunday' and 10 <= hour < 18:
    print('open')
else:
    print('closed')

# По-дълго решение
#
# working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# if day_of_week in working_days and 10 <= hour < 18:
#     print('open')
# else:
#     print('closed')