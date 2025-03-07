tournaments_number = int(input())
start_points = int(input())

finish_status = ''
wins = 0
finalist = 0
semi_finalist = 0
final_points = start_points

for tournament in range(1, tournaments_number + 1):
    finish_status = input().lower() # W, F or SF
    if finish_status == 'w':
        wins += 1
        final_points += 2000
    elif finish_status == 'f':
        finalist += 1
        final_points += 1200
    elif finish_status == 'sf':
        semi_finalist += 1
        final_points += 720

average_points = (final_points - start_points) // tournaments_number
percent_wins = wins / tournaments_number * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{percent_wins:.2f}%')

