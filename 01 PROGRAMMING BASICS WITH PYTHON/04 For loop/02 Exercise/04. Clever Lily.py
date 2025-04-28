lily_years = int(input()) # Lily's years
washing_machine_price = float(input())  # the price of the wanted washing machine
toy_single_price = int(input()) # single price of a toy

total_toys = 0
total_money = 0

for birthday in range(1, lily_years + 1):
    if birthday % 2 != 0:
        total_toys += 1
    else:
        total_money = total_money + (birthday / 2) * 10 - 1 # -1 is for her brother

toy_earnings = total_toys * toy_single_price
total_money = total_money + toy_earnings
money_diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    output = f"Yes! {money_diff:.2f}"
else:
    output = f"No! {money_diff:.2f}"

print(output)


