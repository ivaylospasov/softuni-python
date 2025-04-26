# Read input
strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

# Calculate prices for other fruits
raspberries_price = strawberry_price / 2
oranges_price = raspberries_price * 0.6  # 40% lower than raspberries
bananas_price = raspberries_price * 0.2  # 80% lower than raspberries

# Calculate total cost
total_cost = (strawberry_price * strawberries_kg) + (bananas_price * bananas_kg) + \
             (oranges_price * oranges_kg) + (raspberries_price * raspberries_kg)

# Print the result formatted to 2 decimal places
print(f"{total_cost:.2f}")