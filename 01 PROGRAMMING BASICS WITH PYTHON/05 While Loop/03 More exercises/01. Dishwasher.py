dishwasher_bottles = int(input()) # number of dishwasher bottles

BOTTLE_VOLUME = 750 # The volume of one dishwasher bottle in milliliters.
DETERGENT_PER_DISH = 5 # The amount of detergent needed for one dish.
DETERGENT_PET_POT = 15 # The amount of detergent needed for one pot.

total_detergent = dishwasher_bottles * BOTTLE_VOLUME
cleaned_dishes = 0
cleaned_pots = 0
load_dishes = 0
loads = 0

while total_detergent >= 0:
    load_dishes = input()

    if load_dishes == 'End':
        break
    else:
        load_dishes = int(load_dishes)
        loads += 1
        if loads % 3 == 0:
            cleaned_pots += load_dishes
            total_detergent -= load_dishes * DETERGENT_PET_POT
        else:
            cleaned_dishes += load_dishes
            total_detergent -= load_dishes * DETERGENT_PER_DISH

if total_detergent >= 0:
    print('Detergent was enough!')
    print(f'{cleaned_dishes} dishes and {cleaned_pots} pots were washed.')
    print(f'Leftover detergent {total_detergent} ml.')
else:
    print(f'Not enough detergent, {abs(total_detergent)} ml. more necessary!')