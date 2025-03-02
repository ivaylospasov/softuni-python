# %%
from math import ceil

# %%
tv_series = input()
part_duration = int(input())
break_duration = int(input())

# %%
lunch_duration = break_duration / 8
rest_duration = break_duration / 4

# %%
time_left_to_watch = break_duration - lunch_duration - rest_duration

# %%
if time_left_to_watch >= part_duration:
    break_time_left = ceil(time_left_to_watch - part_duration)
    print(f'You have enough time to watch {tv_series} and left with {break_time_left} minutes free time.')
else:
    time_needed = ceil(part_duration - time_left_to_watch)
    print(f'You don\'t have enough time to watch {tv_series}, you need {time_needed} more minutes.')
