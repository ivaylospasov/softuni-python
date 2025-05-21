TICKET_COST = 150
CLOTHES_MAX_PRICE = 50
SHOES_MAX_PRICE = 35
ACCESSORIES_MAX_PRICE = 20.50

markup = 1.4

goods_as_strings = input().split("|")

goods_as_lists = []

for good in goods_as_strings:
    goods_as_lists.append(good.split("->"))

budget = float(input())

money_spend = 0

new_prices = []

for good in goods_as_lists:
    good_name = good[0]
    good_price = float(good[1])
    if good_price <= budget:
        if (good_name == "Clothes" and good_price <= CLOTHES_MAX_PRICE) \
            or (good_name == "Shoes" and good_price <= SHOES_MAX_PRICE) \
            or (good_name == "Accessories" and good_price <= ACCESSORIES_MAX_PRICE):
            budget -= good_price
            money_spend += good_price
            new_price = good_price * markup
            new_prices.append(new_price)
    else:
        pass

money_earned = budget + sum(new_prices)
profit = sum(new_prices) - money_spend

for price in new_prices:
    print(f"{price:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if money_earned >= TICKET_COST:
    print("Hello, France!")
else:
    print("Not enough money.")