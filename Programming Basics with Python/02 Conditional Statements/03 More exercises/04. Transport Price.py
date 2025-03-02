distance = int(input())
period = input()

taxi_start_tax = 0.7
taxi_day_tariff = 0.79
taxi_night_tariff = 0.9

bus_tariff = 0.09

train_tariff = 0.06

if distance < 20:
    if period == 'day':
        cost = taxi_start_tax + distance * taxi_day_tariff
    else:
        cost = taxi_start_tax + distance * taxi_night_tariff
elif 20 <= distance < 100:
    cost = distance * bus_tariff
else:
    cost = distance * train_tariff

print(f'{cost:.2f}')
