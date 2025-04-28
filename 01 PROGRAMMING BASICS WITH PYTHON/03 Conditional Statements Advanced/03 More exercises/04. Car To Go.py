budget = float(input())
season = input().lower() # Summer or Winter

car_class = ''

if budget <= 100:
    car_class = 'Economy class'
    if season == 'summer':
        car_type = 'Cabrio'
        rent_price = 0.35 * budget
    else:
        car_type = 'Jeep'
        rent_price = 0.65 * budget
elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'summer':
        car_type = 'Cabrio'
        rent_price = 0.45 * budget
    else:
        car_type = 'Jeep'
        rent_price = 0.8 * budget
else:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    rent_price = 0.9 * budget

print(car_class)
print(f'{car_type} - {rent_price:.2f}')