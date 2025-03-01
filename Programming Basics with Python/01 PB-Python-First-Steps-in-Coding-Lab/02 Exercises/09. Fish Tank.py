tank_length = int(input())
tank_width = int(input())
tank_height = int(input())
tank_things_percentage = float(input()) / 100

def cm_to_dm(dimension):
    dimension_dm = dimension / 10
    return dimension_dm

tank_length_dm = cm_to_dm(tank_length)
tank_width_dm = cm_to_dm(tank_width)
tank_height_dm = cm_to_dm(tank_height)

tank_total_volume = tank_length_dm * tank_width_dm * tank_height_dm

tank_water_volume = tank_total_volume - (tank_things_percentage * tank_total_volume)

print(tank_water_volume)
