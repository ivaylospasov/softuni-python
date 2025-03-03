budget = float(input())
season = input().lower()

money_to_spend = 0
destination = ''

if 0 <= budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        money_to_spend = 0.3 * budget
    else:
        money_to_spend = 0.7 * budget
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        money_to_spend = 0.4 * budget
    else:
        money_to_spend = 0.8 * budget
elif 1000 < budget:
    destination = 'Europe'
    money_to_spend = 0.9 * budget

if season == 'summer' and budget <= 1000:
    check_in = 'Camp'
else:
    check_in = 'Hotel'

print(f'Somewhere in {destination.capitalize()}')
print(f'{check_in} - {money_to_spend:.2f}')