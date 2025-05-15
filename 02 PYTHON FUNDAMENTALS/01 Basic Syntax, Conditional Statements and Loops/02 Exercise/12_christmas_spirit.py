quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

ornament_set_price = 2
ornament_set_points = 5

tree_skirt_price = 5
tree_skirt_points = 3

tree_garland_price = 3
tree_garland_points = 10

tree_lights_price = 15
tree_lights_points = 17

total_cost = 0
total_spirit = 0

for day in range(1, days_left_until_christmas + 1):
    if day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        total_spirit += ornament_set_points

    if day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        total_spirit += (tree_skirt_points + tree_garland_points)

    if day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        total_spirit += tree_lights_points
        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        total_cost += (tree_skirt_price + tree_garland_price + tree_lights_price) # buy only one piece of each
        quantity_of_decorations += 2 # the start of the 11th day is the same as the end of the 10th

if days_left_until_christmas % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')
