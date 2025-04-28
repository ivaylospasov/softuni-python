# Read input
days_count = int(input())
total_food = float(input())

# Initialize variables
total_dog_food = 0
total_cat_food = 0
total_biscuits = 0

# Process each day
for day in range(1, days_count + 1):
    # Read daily food consumption
    dog_food = int(input())
    cat_food = int(input())
    
    # Add to total food eaten by each pet
    total_dog_food += dog_food
    total_cat_food += cat_food
    
    # Check if it's the third day for biscuits
    if day % 3 == 0:
        # Calculate biscuits (10% of total food eaten that day)
        daily_biscuits = (dog_food + cat_food) * 0.1
        total_biscuits += daily_biscuits

# Calculate total food eaten
total_eaten_food = total_dog_food + total_cat_food

# Calculate percentages
percent_eaten = (total_eaten_food / total_food) * 100
percent_dog = (total_dog_food / total_eaten_food) * 100
percent_cat = (total_cat_food / total_eaten_food) * 100

# Print results
print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")