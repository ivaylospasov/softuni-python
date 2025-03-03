flowers_type = input().lower()
flowers_number = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.8
tulips_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

total_cost = 0

if flowers_type == 'roses':
    if flowers_number > 80:
        total_cost = (1 - 0.1) * roses_price * flowers_number
    else:
        total_cost = roses_price * flowers_number
elif flowers_type == 'dahlias':
    if flowers_number > 90:
        total_cost = (1 - 0.15) * dahlias_price * flowers_number
    else:
        total_cost = dahlias_price * flowers_number
elif flowers_type == 'tulips':
    if flowers_number > 80:
        total_cost = (1 - 0.15) * tulips_price * flowers_number
    else:
        total_cost = tulips_price * flowers_number
elif flowers_type == 'narcissus':
    if flowers_number < 120:
        total_cost = (1 + 0.15) * narcissus_price * flowers_number
    else:
        total_cost = narcissus_price * flowers_number
elif flowers_type == 'gladiolus':
    if flowers_number < 80:
        total_cost = (1 + 0.2) * gladiolus_price * flowers_number
    else:
        total_cost = gladiolus_price * flowers_number

if budget >= total_cost:
    money_left = budget - total_cost
    print(f'Hey, you have a great garden with '
          f'{flowers_number} {flowers_type.capitalize()} and '
          f'{money_left:.2f} leva left.')
else:
    money_needed = total_cost - budget
    print(f'Not enough money, '
          f'you need {money_needed:.2f} leva more.')