vip_price = 499.99
normal_price = 249.99

budget = int(input())
ticket_category = input().lower() # VIP or Normal
people = int(input())

tickets_price = 0

if ticket_category == 'vip':
    tickets_price = people * vip_price
elif ticket_category == 'normal':
    tickets_price = people * normal_price

transport_cost = 0

if 1 <= people <= 4:
    transport_cost = 0.75 * budget
elif 5 <= people <= 9:
    transport_cost = 0.6 * budget
elif 10 <= people <= 24:
    transport_cost = 0.5 * budget
elif 25 <= people <= 49:
    transport_cost = 0.4 * budget
elif 50 <= people:
    transport_cost = 0.25 * budget

total_cost = transport_cost + tickets_price

if total_cost <= budget:
    money_left = budget - total_cost
    output = f'Yes! You have {money_left:.2f} leva left.'
else:
    money_needed = total_cost - budget
    output = f'Not enough money! You need {money_needed:.2f} leva.'

print(output)