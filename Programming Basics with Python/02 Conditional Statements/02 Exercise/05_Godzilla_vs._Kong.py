budget = float(input())
people = int(input())
clothes_per_person_cost = float(input())

decor = 0.1 * budget
clothes_cost = people * clothes_per_person_cost

if people > 150:
    clothes_cost -= 0.1 * clothes_cost

all_costs = clothes_cost + decor

if budget < all_costs:
    money_needed = all_costs - budget
    print(f'Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')
else:
    money_left = budget - all_costs
    print(f'Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
