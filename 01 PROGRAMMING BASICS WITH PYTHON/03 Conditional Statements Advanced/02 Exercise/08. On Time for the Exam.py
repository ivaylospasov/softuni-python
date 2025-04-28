exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

status = ''
output = ''

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

if exam_time >= arrival_time:
    if exam_time - arrival_time <= 30:
        status = 'On time'
        time_difference = exam_time - arrival_time
        output = f'{time_difference} minutes before the start'
    else:
        status = 'Early'
        time_difference = exam_time - arrival_time
        if time_difference <= 59:
            output = f'{time_difference} minutes before the start'
        else:
            time_difference_hours = time_difference // 60
            time_difference_minutes = time_difference % 60
            output = f'{time_difference_hours}:{time_difference_minutes:02d} hours before the start'
else:
    status = 'Late'
    time_difference = arrival_time - exam_time
    if time_difference <= 59:
        output = f'{time_difference} minutes after the start'
    else:
        time_difference_hours = time_difference // 60
        time_difference_minutes = time_difference % 60
        output = f'{time_difference_hours}:{time_difference_minutes:02d} hours after the start'


print(status)
print(output)