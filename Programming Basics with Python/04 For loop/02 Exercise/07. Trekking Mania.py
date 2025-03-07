group_number = int(input())

total_climbers = 0
climbers_to_musala = 0
climbers_to_monblanc = 0
climbers_to_kilimadjaro = 0
climbers_to_k2 = 0
climbers_to_everest = 0

for group in range(1, group_number + 1):
    climbers_in_group = int(input())
    total_climbers += climbers_in_group
    if climbers_in_group <= 5:
        climbers_to_musala += climbers_in_group
    elif 6 <= climbers_in_group <= 12:
        climbers_to_monblanc += climbers_in_group
    elif 13 <= climbers_in_group <= 25:
        climbers_to_kilimadjaro += climbers_in_group
    elif 26 <= climbers_in_group <= 40:
        climbers_to_k2 += climbers_in_group
    else:
        climbers_to_everest += climbers_in_group

percent_to_musala = (climbers_to_musala / total_climbers) * 100
percent_to_montblanc = (climbers_to_monblanc / total_climbers) * 100
percent_to_kilimandjaro = (climbers_to_kilimadjaro / total_climbers) * 100
percent_to_k2 = (climbers_to_k2 / total_climbers) * 100
percent_to_everest = (climbers_to_everest / total_climbers) * 100

print(f'{percent_to_musala:.2f}%')
print(f'{percent_to_montblanc:.2f}%')
print(f'{percent_to_kilimandjaro:.2f}%')
print(f'{percent_to_k2:.2f}%')
print(f'{percent_to_everest:.2f}%')
