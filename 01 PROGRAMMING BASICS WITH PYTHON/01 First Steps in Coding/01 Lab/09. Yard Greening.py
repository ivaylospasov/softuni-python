area: float = float(input())

price_for_sq_m: float = 7.61

total_price: float = area * price_for_sq_m
total_discount = 0.18 * total_price
price_with_discount = total_price - total_discount

print(f'The final price is: {price_with_discount} lv.')
print(f'The discount is: {total_discount} lv.')