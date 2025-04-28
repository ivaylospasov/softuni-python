junior_bikers = int(input())
senior_bikers = int(input())
type_race = input().lower()

total_participants = junior_bikers + senior_bikers
junior_tax = 0
senior_tax = 0

if type_race == 'trail':
    junior_tax = 5.5
    senior_tax = 7
elif type_race == 'cross-country':
    junior_tax = 8
    senior_tax = 9.5
    if total_participants >= 50:
        junior_tax = (1 - 0.25) * junior_tax
        senior_tax = (1 - 0.25) * senior_tax
elif type_race == 'downhill':
    junior_tax = 12.25
    senior_tax = 13.75
elif type_race == 'road':
    junior_tax = 20
    senior_tax = 21.5

total_amount = junior_bikers * junior_tax + senior_bikers * senior_tax

# Organisational taxes 5%
amount_for_taxes = 0.05 * total_amount

total_amount_after_taxes = total_amount - amount_for_taxes

print(f'{total_amount_after_taxes: .2f}')
