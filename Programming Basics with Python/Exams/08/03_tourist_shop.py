budget = float(input())
product_count = 0
total_cost = 0
is_budget_enough = True

while True:
    product_name = input()

    if product_name == 'Stop':
        break

    product_price = float(input())

    # Apply discount for every third product
    if (product_count + 1) % 3 == 0:
        product_price /= 2

    # Check if budget is enough
    if product_price > budget:
        is_budget_enough = False
        needed_money = product_price - budget
        break

    # Purchase the product
    budget -= product_price
    total_cost += product_price
    product_count += 1

if is_budget_enough:
    print(f'You bought {product_count} products for {total_cost:.2f} leva.')
else:
    print(f"You don't have enough money!")
    print(f'You need {needed_money:.2f} leva!')
