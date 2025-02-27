dog_food_packs: int = int(input(f'Enter the number of dog food packs you will buy: '))
cat_food_packs: int = int(input(f'Enter the number of cat food packs you will buy: '))

food_total_sum: float = dog_food_packs * 2.5 + cat_food_packs * 4

print(f'Total sum: {food_total_sum} lv.')