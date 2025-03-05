from math import floor

year_type = input().lower() # leap or normal
holidays = int(input()) # празници
weekends_at_home = int(input())

weekends_in_sofia = 48 - weekends_at_home
play_in_sofia = 3 / 4 * weekends_in_sofia + 2 / 3 * holidays

total_play = play_in_sofia + weekends_at_home

if year_type == 'leap':
    total_play = (1 + 0.15) * total_play

print(floor(total_play))