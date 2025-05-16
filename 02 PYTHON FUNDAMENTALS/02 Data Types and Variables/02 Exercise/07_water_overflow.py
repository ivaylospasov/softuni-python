n = int(input())
water_to_pour = 0

TANK_CAPACITY = 255

for litres in range(n):
    litres_of_water = int(input())
    if litres_of_water > TANK_CAPACITY:
        print("Insufficient capacity!")
    else:
        TANK_CAPACITY -= litres_of_water
        water_to_pour += litres_of_water

print(water_to_pour)
