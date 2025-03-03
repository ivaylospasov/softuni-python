budget = int(input())
season = input().lower()
fisherman_number = int(input())

spring_rent = 3000
summer_rent = 4200
autumn_rent = summer_rent
winter_rent = 2600

boat_rent = 0

if season == 'spring':
    if fisherman_number <= 6:
        boat_rent = (1 - 0.1) * spring_rent
    elif 7 <= fisherman_number <= 11:
        boat_rent = (1 - 0.15) * spring_rent
    elif 12 <= fisherman_number:
        boat_rent = (1 - 0.25) * spring_rent
elif season == 'summer' or season == 'autumn':
    if fisherman_number <= 6:
        boat_rent = (1 - 0.1) * summer_rent
    elif 7 <= fisherman_number <= 11:
        boat_rent = (1 - 0.15) * summer_rent
    elif 12 <= fisherman_number:
        boat_rent = (1 - 0.25) * summer_rent
elif season == 'winter':
    if fisherman_number <= 6:
        boat_rent = (1 - 0.1) * winter_rent
    elif 7 <= fisherman_number <= 11:
        boat_rent = (1 - 0.15) * winter_rent
    elif 12 <= fisherman_number:
        boat_rent = (1 - 0.25) * winter_rent

if fisherman_number % 2 == 0 and season != 'autumn':
    boat_rent = (1 - 0.05) * boat_rent

if budget >= boat_rent:
    money_left = budget - boat_rent
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = boat_rent - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')