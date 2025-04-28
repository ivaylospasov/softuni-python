days_to_stay = int(input())
room_type = input().lower()
feedback = input().lower() # positive or negative

nights_number = days_to_stay - 1

room_price = 18
apartment_price = 25
president_apartment_price = 35

if days_to_stay < 10:
    if room_type == 'room for one person':
        total_cost = nights_number * room_price
    elif room_type == 'apartment':
        total_cost = (1 - 0.3) * nights_number * apartment_price
    else:
        total_cost = (1 - 0.1) * nights_number * president_apartment_price
elif 10 <= days_to_stay <= 15:
    if room_type == 'room for one person':
        total_cost = nights_number * room_price
    elif room_type == 'apartment':
        total_cost = (1 - 0.35) * nights_number * apartment_price
    else:
        total_cost = (1 - 0.15) * nights_number * president_apartment_price
else:
    if room_type == 'room for one person':
        total_cost = nights_number * room_price
    elif room_type == 'apartment':
        total_cost = (1 - 0.5) * nights_number * apartment_price
    else:
        total_cost = (1 - 0.2) * nights_number * president_apartment_price

if feedback == 'positive':
    total_cost = (1 + 0.25) * total_cost
elif feedback == 'negative':
    total_cost = (1 - 0.1) * total_cost

print(f'{total_cost:.2f}')