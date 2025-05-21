fire_level_strings = input().split("#")
water = int(input())

fire_levels_as_lists = []
seized_fire_cells = []
total_fire = 0
effort = 0

for string in fire_level_strings:
    fire_levels_as_lists.append(string.split(" = "))

for level in fire_levels_as_lists:
    fire_type = level[0]
    water_needed = int(level[1])
    if (fire_type == "High" and 81 <= water_needed <= 125) \
        or (fire_type == "Medium" and 51 <= water_needed <= 80) \
        or (fire_type == "Low" and 1 <= water_needed <= 50):
        if water >= water_needed:
            water -= water_needed
            effort += water_needed * 0.25
            total_fire += water_needed
            seized_fire_cells.append(water_needed)
        else:
            break

print("Cells:")
for cell in seized_fire_cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")