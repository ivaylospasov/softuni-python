family_budget = float(input())
nights_count = int(input())
price_per_night = float(input())
additional_cost_percent = int(input())

if nights_count > 7:
    price_per_night = price_per_night * 0.95
    #print(price_per_night)

vacation_total_cost = nights_count * price_per_night + family_budget * additional_cost_percent / 100

if vacation_total_cost <= family_budget:
    money_left = family_budget - vacation_total_cost
    print(f'Ivanovi will be left with {money_left:.2f} leva after vacation.')
else:
    money_needed = abs(family_budget - vacation_total_cost)
    print(f'{money_needed:.2f} leva needed.')