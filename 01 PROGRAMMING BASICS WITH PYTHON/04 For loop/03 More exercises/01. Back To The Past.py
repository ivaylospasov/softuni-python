age = 18

heritage_money = float(input())
year_to_live = int(input())

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        heritage_money -= 12000
        age += 1
    else:
        heritage_money = heritage_money - (12000 + 50 * age)
        age += 1

if heritage_money >= 0:
    print(f'Yes! He will live a carefree life and will have {heritage_money:.2f} dollars left.')
else:
    print(f'He will need {abs(heritage_money):.2f} dollars to survive.')