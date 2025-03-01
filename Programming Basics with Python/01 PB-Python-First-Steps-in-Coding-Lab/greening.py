area: float = float(input('Enter the area for landscaping: '))

price_for_sq_m = 7.61

total_price = area * price_for_sq_m
total_discount = 0.18 * total_price
price_with_discount = total_price - total_discount

print(f'The final price is: {price_with_discount} lv.')
print(f'The discount is: {total_discount} lv.')