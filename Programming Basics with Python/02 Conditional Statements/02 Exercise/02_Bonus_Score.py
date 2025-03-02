my_score = int(input())

# Моето решение
# if my_score <= 100:
#     bonus_points = 5
# elif 100 <= my_score <= 1000:
#     bonus_points = 0.2 * my_score
# elif 1000 < my_score:
#     bonus_points = 0.1 * my_score
#
# if my_score % 2 == 0:
#     additional_points = 1
# elif my_score % 5 == 0 and my_score % 2 != 0:
#     additional_points = 2
# else:
#     additional_points = 0
#
# all_bonus_points = bonus_points + additional_points
# total_score = my_score + all_bonus_points
#
# print(all_bonus_points)
# print(total_score)

# Алтернативно по-добро и кратко решение от обясненията
if my_score <= 100:
    bonus_points = 5
elif 100 <= my_score <= 1000:
    bonus_points = 0.2 * my_score
elif 1000 < my_score:
    bonus_points = 0.1 * my_score

if my_score % 2 == 0:
    bonus_points += 1
elif my_score % 10 == 5: # Ако разделим числото на 10, получаваме остатък 5
    bonus_points += 2

print(bonus_points)
print(my_score + bonus_points)