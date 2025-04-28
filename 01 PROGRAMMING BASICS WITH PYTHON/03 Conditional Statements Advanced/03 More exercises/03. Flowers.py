chrysanthemum_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input().lower()  # Spring, Summer, Autumn, Winter
is_official_holiday = input().lower()  # Y – да / N - не

flowers = ['chrysanthemum', 'roses', 'tulips']
all_flowers = sum([chrysanthemum_number, roses_number, tulips_number])


if season == 'spring' or season == 'summer':
    chrysanthemum_price = 2
    roses_price = 4.1
    tulips_price = 2.5
    if is_official_holiday == 'y':
        chrysanthemum_price = (1 + 0.15) * chrysanthemum_price
        roses_price = (1 + 0.15) * roses_price
        tulips_price = (1 + 0.15) * tulips_price
else:
    chrysanthemum_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
    if is_official_holiday == 'y':
        chrysanthemum_price = (1 + 0.15) * chrysanthemum_price
        roses_price = (1 + 0.15) * roses_price
        tulips_price = (1 + 0.15) * tulips_price

total_price_chrysanthemum = chrysanthemum_number * chrysanthemum_price
total_price_roses = roses_number * roses_price
total_price_tulips = tulips_number * tulips_price

total_price = sum([total_price_chrysanthemum, total_price_roses, total_price_tulips])

if season == 'spring' and tulips_number > 7:
    total_price = (1 - 0.05) * total_price

if season == 'winter' and roses_number >= 10:
    total_price = (1 - 0.1) * total_price

if all_flowers > 20:
    total_price = (1 - 0.2) * total_price

# Always add at the end
flowers_arrange = 2

total_price = total_price + flowers_arrange

print(f'{total_price:.2f}')