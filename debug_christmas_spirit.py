quantity_of_decorations = 1
days_left_until_christmas = 10

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

print("Day | Cost | Spirit | Quantity | Action")
print("-" * 50)

for day in range(1, days_left_until_christmas + 1):
    actions = []
    
    # Check if it's the 11th day to increase quantity
    if day % 11 == 0:
        quantity_of_decorations += 2
        actions.append("Quantity +2")

    # Every second day buy Ornament Sets
    if day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        total_spirit += ornament_set_points
        actions.append(f"Ornament Set (+{ornament_set_price * quantity_of_decorations}$, +{ornament_set_points} spirit)")

    # Every third day buy Tree Skirts and Tree Garlands
    if day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        total_spirit += (tree_skirt_points + tree_garland_points)
        actions.append(f"Tree Skirt + Garland (+{(tree_skirt_price + tree_garland_price) * quantity_of_decorations}$, +{tree_skirt_points + tree_garland_points} spirit)")

    # Every fifth day buy Tree Lights
    if day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        total_spirit += tree_lights_points
        actions.append(f"Tree Lights (+{tree_lights_price * quantity_of_decorations}$, +{tree_lights_points} spirit)")
        
        # If you have bought Tree Lights and Tree Garlands on the same day
        if day % 3 == 0:
            total_spirit += 30
            actions.append("Lights + Garland bonus (+30 spirit)")

    # Every tenth day your cat ruins all tree decorations
    if day % 10 == 0:
        total_spirit -= 20
        # Buy one piece of each decoration (not quantity_of_decorations pieces)
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
        actions.append(f"Cat ruins decorations (-20 spirit, +{tree_skirt_price + tree_garland_price + tree_lights_price}$ for 1 of each)")

    print(f"{day:2d} | {total_cost:3d} | {total_spirit:3d} | {quantity_of_decorations:8d} | {', '.join(actions)}")

# If the last day is the tenth day, lose additional 30 spirit
if days_left_until_christmas % 10 == 0:
    total_spirit -= 30
    print(f"Last day is 10th: -30 spirit")

print("-" * 50)
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

# Now for 11 days
print("\n\nRunning for 11 days:")
quantity_of_decorations = 1
days_left_until_christmas = 11
total_cost = 0
total_spirit = 0

print("Day | Cost | Spirit | Quantity | Action")
print("-" * 50)

for day in range(1, days_left_until_christmas + 1):
    actions = []
    
    # Check if it's the 11th day to increase quantity
    if day % 11 == 0:
        quantity_of_decorations += 2
        actions.append("Quantity +2")

    # Every second day buy Ornament Sets
    if day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        total_spirit += ornament_set_points
        actions.append(f"Ornament Set (+{ornament_set_price * quantity_of_decorations}$, +{ornament_set_points} spirit)")

    # Every third day buy Tree Skirts and Tree Garlands
    if day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        total_spirit += (tree_skirt_points + tree_garland_points)
        actions.append(f"Tree Skirt + Garland (+{(tree_skirt_price + tree_garland_price) * quantity_of_decorations}$, +{tree_skirt_points + tree_garland_points} spirit)")

    # Every fifth day buy Tree Lights
    if day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        total_spirit += tree_lights_points
        actions.append(f"Tree Lights (+{tree_lights_price * quantity_of_decorations}$, +{tree_lights_points} spirit)")
        
        # If you have bought Tree Lights and Tree Garlands on the same day
        if day % 3 == 0:
            total_spirit += 30
            actions.append("Lights + Garland bonus (+30 spirit)")

    # Every tenth day your cat ruins all tree decorations
    if day % 10 == 0:
        total_spirit -= 20
        # Buy one piece of each decoration (not quantity_of_decorations pieces)
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
        actions.append(f"Cat ruins decorations (-20 spirit, +{tree_skirt_price + tree_garland_price + tree_lights_price}$ for 1 of each)")

    print(f"{day:2d} | {total_cost:3d} | {total_spirit:3d} | {quantity_of_decorations:8d} | {', '.join(actions)}")

# If the last day is the tenth day, lose additional 30 spirit
if days_left_until_christmas % 10 == 0:
    total_spirit -= 30
    print(f"Last day is 10th: -30 spirit")

print("-" * 50)
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")