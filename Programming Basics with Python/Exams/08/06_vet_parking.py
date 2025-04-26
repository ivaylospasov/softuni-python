days_count = int(input())
hours_count = int(input())
total_day_cost = 0
total_cost = 0

for day in range(1, days_count + 1):
    for hour in range(1, hours_count + 1):
        if day % 2 == 0 and hour % 2 != 0:
            total_day_cost += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            total_day_cost += 1.25
        else:
            total_day_cost += 1
    total_cost += total_day_cost
    print(f'Day: {day} - {total_day_cost:.2f} leva')
    total_day_cost = 0

print(f'Total: {total_cost:.2f} leva')