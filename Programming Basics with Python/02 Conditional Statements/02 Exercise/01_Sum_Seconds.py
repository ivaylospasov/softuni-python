time_first = int(input())
time_second = int(input())
time_third = int(input())

time_sum = sum([time_first, time_second, time_third])

minutes = time_sum // 60
seconds = time_sum % 60

print(f'{minutes}:{seconds:02d}')

# # Алтернативно решение с if else
# if seconds < 10:
#     print(f'{minutes}:0{seconds}')
# else:
#     print(f'{minutes}:{seconds}')

