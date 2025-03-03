fuel_type = input() # Diesel, Gasoline, Gas
fuel_litres = int(input())

if fuel_type == 'Diesel' or fuel_type == 'Gasoline' or fuel_type == 'Gas':
    fuel_type = fuel_type.casefold()
    if 25 <= fuel_litres:
        print(f'You have enough {fuel_type}.')
    else:
        print(f'Fill your tank with {fuel_type}!')
else:
    print('Invalid fuel!')

