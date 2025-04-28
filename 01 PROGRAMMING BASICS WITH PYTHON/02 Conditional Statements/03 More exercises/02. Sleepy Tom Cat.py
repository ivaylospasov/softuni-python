# %%
holidays_a_year = int(input())

# %%
play_minutes_a_year = 30000
play_minutes_work_day = 63
play_minutes_holiday = 127

# %%
workdays_a_year = 365 - holidays_a_year
workday_total_play_minutes = workdays_a_year * play_minutes_work_day
holiday_total_play_minutes = holidays_a_year * play_minutes_holiday
total_play_minutes_a_year = workday_total_play_minutes + holiday_total_play_minutes

# %%
if total_play_minutes_a_year > play_minutes_a_year:
    play_overtime = total_play_minutes_a_year - play_minutes_a_year
    play_hours_overtime = play_overtime // 60
    play_minutes_overtime = play_overtime % 60
    print(f'Tom will run away')
    print(f'{play_hours_overtime} hours and {play_minutes_overtime} minutes more for play')
else:
    play_time_difference = play_minutes_a_year - total_play_minutes_a_year
    play_hours_difference = play_time_difference // 60
    play_minutes_difference = play_time_difference % 60
    print(f'Tom sleeps well')
    print(f'{play_hours_difference} hours and {play_minutes_difference} minutes less for play')
