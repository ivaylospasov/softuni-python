from math import ceil

DISTANCE = 384400
TIME_ON_THE_MOON = 3

speed = float(input())
fuel_per_100km = float(input())

total_distance = DISTANCE * 2

total_time_traveling = ceil(total_distance / speed)

total_time_in_space = total_time_traveling + TIME_ON_THE_MOON

total_fuel = (total_distance / 100) * fuel_per_100km

print(total_time_in_space)
print(int(total_fuel))