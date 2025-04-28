location_count = int(input())

total_gold_mined = 0
real_average_gold_per_day = 0

for location in range(location_count):
    expected_gold_per_day = float(input())
    days_count = int(input())
    for day in range(days_count):
        real_gold_per_day = float(input())
        total_gold_mined += real_gold_per_day

    real_average_gold_per_day = total_gold_mined / days_count
    if real_average_gold_per_day >= expected_gold_per_day:
        print(f'Good job! Average gold per day: {real_average_gold_per_day:.2f}.')
    else:
        gold_diff = abs(real_average_gold_per_day - expected_gold_per_day)
        print(f'You need {gold_diff:.2f} gold.')

    total_gold_mined = 0 # reset total gold mined
