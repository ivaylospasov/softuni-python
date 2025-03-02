chicken_prise = 10.35
fish_prise = 12.4
vegan_prise = 8.15
delivery_prise = 2.5

chicken_orders = int(input())
fish_orders = int(input())
vegan_orders = int(input())

chicken_cost = chicken_prise * chicken_orders
fish_cost = fish_prise * fish_orders
vegan_cost = vegan_prise * vegan_orders

all_meals_costs = [chicken_cost, fish_cost, vegan_cost]
total_meals_costs = sum(all_meals_costs)

desert_cost = 0.2 * total_meals_costs

total_cost = total_meals_costs + desert_cost + delivery_prise

print(total_cost)