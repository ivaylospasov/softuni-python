from pywin.tools.TraceCollector import outputWindow

exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

# if ((arrival_hour == exam_hour and 0 <= (exam_minute - arrival_minute) <= 30) or
#         ((exam_hour - arrival_hour) == 1 and (exam_minute + 60 - arrival_minute) <= 30)):
#     print('Student on time for the exam')

# TODO Да пробвам да изчисля времето в минути, след като представя часовете и след това да извадя стойностите

if arrival_hour == exam_hour:
    if arrival_minute < exam_minute:
        if exam_minute - arrival_minute <= 30:
            status = 'On time'
        else:
            status = 'Early'
        minutes_difference = exam_minute - arrival_minute
        output = f'{minutes_difference} minutes before the start'
    elif arrival_minute > exam_minute:
        status = 'Late'
        minutes_difference = arrival_minute - exam_minute
        output = f'{minutes_difference} minutes after the start'
elif arrival_hour > exam_hour:
    status = 'Late'
    if arrival_hour - exam_hour == 1:
        pass

print(status)
print(output)