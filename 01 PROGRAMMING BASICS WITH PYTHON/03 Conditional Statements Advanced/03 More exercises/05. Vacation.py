budget: float = float(input())
season = input().lower() # Summer or Winter

stay_in = ''

if budget <= 1000:
    stay_in = 'Camp'
    if season == 'summer':
        location = 'Alaska'
        cost = 0.65 * budget
    else:
        location = 'Morocco'
        cost = 0.45 * budget
elif 1000 < budget <= 3000:
    stay_in = 'Hut'
    if season == 'summer':
        location = 'Alaska'
        cost = 0.8 * budget
    else:
        location = 'Morocco'
        cost = 0.6 * budget
else:
    stay_in = 'Hotel'
    cost = 0.9 * budget
    if season == 'summer':
        location = 'Alaska'
    else:
        location = 'Morocco'

print(f'{location.capitalize()} - {stay_in} - {cost:.2f}')