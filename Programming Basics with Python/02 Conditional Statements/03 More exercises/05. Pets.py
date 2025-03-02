from math import ceil, floor

number_of_days = int(input())
food_left = int(input())
dog_kg_food_per_day_needed = float(input())
cat_kg_food_per_day_needed = float(input())
turtle_gr_food_per_day_needed = float(input())

dog_food = dog_kg_food_per_day_needed * number_of_days
cat_food = cat_kg_food_per_day_needed * number_of_days
turtle_food = turtle_gr_food_per_day_needed * number_of_days / 1000

total_food = sum([dog_food, cat_food, turtle_food])

if total_food <= food_left:
    food_extra = floor(food_left - total_food)
    print(f'{food_extra} kilos of food left.')
else:
    food_missing = ceil(total_food - food_left)
    print(f'{food_missing} more kilos of food are needed.')