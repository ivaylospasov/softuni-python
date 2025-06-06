cards_list = input().split()

TEAM_A_PLAYERS_COUNT = 11
TEAM_B_PLAYERS_COUNT = 11

team_a_cards = set()
team_b_cards = set()

if len(cards_list) != 0:
    for card in cards_list:
        if card[0] == 'A':
            team_a_cards.add(card)
            if len(team_a_cards) > 4:
                break
        else:
            team_b_cards.add(card)
            if len(team_b_cards) > 4:
                break

    team_a_players_last = TEAM_A_PLAYERS_COUNT - len(team_a_cards)
    team_b_players_last = TEAM_B_PLAYERS_COUNT - len(team_b_cards)

    if team_a_players_last < 7 or team_b_players_last < 7:
        print(f"Team A - {team_a_players_last}; Team B - {team_b_players_last}")
        print("Game was terminated")
    else:
        print(f"Team A - {team_a_players_last}; Team B - {team_b_players_last}")
else:
    print(f"Team A - {TEAM_A_PLAYERS_COUNT}; Team B - {TEAM_B_PLAYERS_COUNT}")


# Alternative with list only

# team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
#
# game_terminated = False
#
# players = input().split()
#
# for player in players:
#     if player in team_a:
#         team_a.remove(player)
#     elif player in team_b:
#         team_b.remove(player)
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_terminated = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if game_terminated:
#     print("Game was terminated")