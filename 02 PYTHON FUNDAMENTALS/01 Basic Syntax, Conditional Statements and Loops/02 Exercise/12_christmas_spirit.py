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
    # Check if it's the 11th day to increase quantity
    if day % 11 == 0:
        quantity_of_decorations += 2  # increase quantity at the beginning of every 11th day

    # Every second day buy Ornament Sets
    if day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        total_spirit += ornament_set_points

    # Every third day buy Tree Skirts and Tree Garlands
    if day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        total_spirit += (tree_skirt_points + tree_garland_points)

    # Every fifth day buy Tree Lights
    if day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        total_spirit += tree_lights_points
        # If you have bought Tree Lights and Tree Garlands on the same day
        if day % 3 == 0:
            total_spirit += 30

    # Every tenth day your cat ruins all tree decorations
    if day % 10 == 0:
        total_spirit -= 20
        # Buy one piece of each decoration (not quantity_of_decorations pieces)
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price

# If the last day is the tenth day, lose additional 30 spirit
if days_left_until_christmas % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')
