# Read input
annual_fee = int(input())

# Calculate equipment costs
shoes_price = annual_fee * 0.6  # 40% less than annual fee
outfit_price = shoes_price * 0.8  # 20% less than shoes price
ball_price = outfit_price * 0.25  # 1/4 of outfit price
accessories_price = ball_price * 0.2  # 1/5 of ball price

# Calculate total expenses (annual fee + all equipment)
total_expenses = annual_fee + shoes_price + outfit_price + ball_price + accessories_price

# Print the result formatted to 2 decimal places
print(f"{total_expenses:.2f}")