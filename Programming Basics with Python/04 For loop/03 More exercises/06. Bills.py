months = int(input())

water = 20 # a month
internet = 15 # a month

all_electricity = 0
all_water = months * water
all_internet = months * internet
all_other = 0

for month in range(1, months + 1):
    electricity = float(input())
    all_electricity += electricity
    other = (1 + 0.2) * (electricity + water + internet)
    all_other += other


average = (all_electricity + all_water + all_internet + all_other) / months

print(f'Electricity: {all_electricity:.2f} lv')
print(f'Water: {all_water:.2f} lv')
print(f'Internet: {all_internet:.2f} lv')
print(f'Other: {all_other:.2f} lv')
print(f'Average: {average:.2f} lv')