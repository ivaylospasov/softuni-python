my_string = input().lower()

water = 'water'
sun = 'sun'
fish = 'fish'
sand = 'sand'

water_count = my_string.count(water)
sun_count = my_string.count(sun)
fish_count = my_string.count(fish)
sand_count = my_string.count(sand)

all_strings_count = water_count + sun_count + fish_count + sand_count

print(all_strings_count)