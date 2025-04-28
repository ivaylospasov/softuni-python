PETROL_PRICE = 2.10
TUTOR_PRICE = 100
SATURDAY_DISCOUNT = 0.1
SUNDAY_DISCOUNT = 0.2

budget = float(input())
petrol_liters = float(input())
day_of_the_week = input().lower()

total_petrol_cost = petrol_liters * PETROL_PRICE

if day_of_the_week == 'saturday':
    safary_total_cost = (total_petrol_cost + TUTOR_PRICE) * (1 - SATURDAY_DISCOUNT)
else:
    safary_total_cost = (total_petrol_cost + TUTOR_PRICE) * (1 - SUNDAY_DISCOUNT)

money_differece = abs(budget - safary_total_cost)

if safary_total_cost <= budget:
    print(f'Safari time! Money left: {money_differece:.2f} lv. ')
else:
    print(f'Not enough money! Money needed: {money_differece:.2f} lv.')
