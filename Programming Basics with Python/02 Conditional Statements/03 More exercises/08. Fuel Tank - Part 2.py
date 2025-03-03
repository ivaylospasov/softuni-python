# Fuel prices
gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

# Fuel discounts with a club card
gasoline_card_discount_price = 0.18
diesel_card_discount_price = 0.12
gas_card_discount_price = 0.08

# 8% discount if fuel is over to 20 (included) but not over 25l
quantity_discount_percent_one = 0.08
# 8% discount if fuel is over 25l
quantity_discount_percent_two = 0.1

fuel_type = input() # Diesel, Petrol, Gas
fuel_quantity = float(input())
has_club_card = input() # Yes, No

if fuel_type == 'Gasoline':
    if has_club_card == 'Yes':
        new_fuel_price = gasoline_price - gasoline_card_discount_price
        total_cost = fuel_quantity * new_fuel_price
    else:
        total_cost = fuel_quantity * gasoline_price
elif fuel_type == 'Diesel':
    if has_club_card == 'Yes':
        new_fuel_price = diesel_price - diesel_card_discount_price
        total_cost = fuel_quantity * new_fuel_price
    else:
        total_cost = fuel_quantity * diesel_price
else:
    if has_club_card == 'Yes':
        new_fuel_price = gas_price - gas_card_discount_price
        total_cost = fuel_quantity * new_fuel_price
    else:
        total_cost = fuel_quantity * gas_price

if 20 <= fuel_quantity <= 25:
    total_cost = (1 - quantity_discount_percent_one) * total_cost
elif 25 < fuel_quantity:
    total_cost = (1 - quantity_discount_percent_two) * total_cost

print(f'{total_cost:.2f} lv.')