CAT_FOOD_PRICE_PER_KG = 12.45

cat_count = int(input())

total_food_group_1 = 0
total_food_group_2 = 0
total_food_group_3 = 0

total_cats_group_1 = 0
total_cats_group_2 = 0
total_cats_group_3 = 0

for cat in range(cat_count):
    food_eaten_in_grams = float(input())
    if 100 <= food_eaten_in_grams < 200:
        total_food_group_1 += food_eaten_in_grams
        total_cats_group_1 += 1
    elif 200 <= food_eaten_in_grams < 300:
        total_food_group_2 += food_eaten_in_grams
        total_cats_group_2 += 1
    elif 300 <= food_eaten_in_grams < 400:
        total_food_group_3 += food_eaten_in_grams
        total_cats_group_3 += 1

total_food_eaten = (total_food_group_1 + total_food_group_2 + total_food_group_3) / 1000
total_cost_per_day = total_food_eaten * CAT_FOOD_PRICE_PER_KG

print(f'Group 1: {total_cats_group_1} cats.')
print(f'Group 2: {total_cats_group_2} cats.')
print(f'Group 3: {total_cats_group_3} cats.')
print(f'Price for food per day: {total_cost_per_day:.2f} lv.')
