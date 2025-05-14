budget = float(input())
flower_price_per_kg = float(input())

pack_of_eggs_price = 0.75 * flower_price_per_kg
milk_per_litre_price = 1.25 * flower_price_per_kg # use only 250 ml per bread

bread_count = 0
colored_eggs_count = 0

one_bread_costs = flower_price_per_kg + pack_of_eggs_price + milk_per_litre_price / 4

while budget >= one_bread_costs:
    budget -= one_bread_costs
    bread_count += 1
    colored_eggs_count += 3
    if bread_count % 3 == 0:
        colored_eggs_count -= bread_count - 2

print(f'You made {bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.')