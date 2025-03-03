month = input().lower()
nights = int(input())

stay_price_in_studio = 0
stay_price_in_apartment = 0

if month == 'may' or month == 'october':
    studio_price = 50
    apartment_price = 65
    stay_price_in_studio = studio_price * nights
    stay_price_in_apartment = apartment_price * nights
    if 7 < nights <= 14:
        stay_price_in_studio = (1 - 0.05) * stay_price_in_studio
    elif 14 < nights:
        stay_price_in_studio = (1 - 0.3) * stay_price_in_studio
        stay_price_in_apartment = (1 - 0.1) * stay_price_in_apartment
elif month == 'june' or month == 'september':
    studio_price = 75.2
    apartment_price = 68.7
    stay_price_in_studio = studio_price * nights
    stay_price_in_apartment = apartment_price * nights
    if 14 < nights:
        stay_price_in_studio = (1 - 0.2) * stay_price_in_studio
        stay_price_in_apartment = (1 - 0.1) * stay_price_in_apartment
elif month == 'july' or month == 'august':
    studio_price = 76
    apartment_price = 77
    stay_price_in_studio = studio_price * nights
    stay_price_in_apartment = apartment_price * nights
    if 14 < nights:
        stay_price_in_apartment = (1 - 0.1) * stay_price_in_apartment

print(f'Apartment: {stay_price_in_apartment:.2f} lv.')
print(f'Studio: {stay_price_in_studio:.2f} lv.')