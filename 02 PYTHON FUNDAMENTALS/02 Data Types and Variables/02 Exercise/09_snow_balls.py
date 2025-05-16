snowballs = int(input())
highest_value = 0
highest_time = 0
highest_quality = 0
highest_weight = 0

for snowball in range(1, snowballs + 1):
    snowball_weight = int(input())
    snowball_time_to_target = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_weight / snowball_time_to_target) ** snowball_quality)
    if snowball_value > highest_value:
        highest_weight = snowball_weight
        highest_value = snowball_value
        highest_time = snowball_time_to_target
        highest_quality = snowball_quality

print(f"{highest_weight} : {highest_time} = {highest_value} ({highest_quality})")
