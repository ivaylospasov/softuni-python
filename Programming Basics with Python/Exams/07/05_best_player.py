best_player_name = ''
best_score = 0
make_hat_trick = False

while True:
    player_name = input()

    if player_name == 'END':
        break

    player_score = int(input())

    if player_score > best_score:
        best_player_name = player_name
        best_score = player_score
        if player_score >= 3:
            make_hat_trick == True

    if player_score >= 10:
        break

print(f'Best player: {best_player_name}')

if make_hat_trick:
    print(f'He has scored {best_score} goals and made a hat-trick !!!')