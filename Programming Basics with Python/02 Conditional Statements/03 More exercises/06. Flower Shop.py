
from math import ceil, floor

number_magnolia = int(input())
number_zyumbyul = int(input())
number_roza = int(input())
number_kaktus = int(input())
present_price = float(input())

magnolia_price = 3.25
zyumbyul_price = 4
roza_price = 3.5
kaktus_price = 8

magnolia_profit = number_magnolia * magnolia_price
zyumbyul_profit = number_zyumbyul * zyumbyul_price
roza_profit = number_roza * roza_price
kaktus_profit = number_kaktus * kaktus_price

tax_percent = 5

total_profit = sum([magnolia_profit, zyumbyul_profit, roza_profit, kaktus_profit])
profit_after_taxes = (1 - tax_percent / 100) * total_profit

if profit_after_taxes >= present_price:
    money_left = floor(profit_after_taxes - present_price)
    print(f'She is left with {money_left} leva.')
else:
    money_needed = ceil(present_price - profit_after_taxes)
    print(f'She will have to borrow {money_needed} leva.')