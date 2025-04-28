season = input().lower() # "Spring", "Summer", "Autumn" or "Winter"
km_per_month = float(input())

earn_per_km = 0

if km_per_month <= 5000:
    if season == 'spring' or season == 'autumn':
        earn_per_km = 0.75
    elif season == 'summer':
        earn_per_km = 0.90
    elif season == 'winter':
        earn_per_km = 1.05
elif 5000 < km_per_month <= 10000:
    if season == 'spring' or season == 'autumn':
        earn_per_km = 0.95
    elif season == 'summer':
        earn_per_km = 1.1
    elif season == 'winter':
        earn_per_km = 1.25
elif 10000 < km_per_month <= 20000:
    earn_per_km = 1.45

total_earnings_per_season = (earn_per_km * km_per_month) * 4

taxes = 0.1 * total_earnings_per_season

total_earnings_per_season = total_earnings_per_season - taxes

print(f'{total_earnings_per_season:.2f}')