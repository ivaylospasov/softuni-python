GAME_END_COMMAND = "END"
HAT_TRICK_THRESHOLD = 3
MAX_SCORE_THRESHOLD = 10

best_player_name = ""
best_score = 0
has_hat_trick = False

while True:
    current_player = input()
    if current_player == GAME_END_COMMAND:
        break

    current_score = int(input())

    if current_score > best_score:
        best_player_name = current_player
        best_score = current_score

        if current_score >= HAT_TRICK_THRESHOLD:
            has_hat_trick = True

    if current_score >= MAX_SCORE_THRESHOLD:
        break

print(f'{best_player_name} is the best player!')

if has_hat_trick:
    print(f'He has scored {best_score} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_score} goals.')