current_product = input()
current_quantity = int(input())

coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00

def total_cost(product, quantity):
    cost = None
    if product == "coffee":
        cost = coffee_price * quantity
    elif product == "water":
        cost = water_price * quantity
    elif product == "coke":
        cost = coke_price * quantity
    elif product == "snacks":
        cost = snacks_price * quantity
    return cost

print(f'{total_cost(current_product, current_quantity):.2f}')
