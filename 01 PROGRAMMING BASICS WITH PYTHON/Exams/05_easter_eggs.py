player_one_eggs = int(input())
player_two_eggs = int(input())

command = input()

while command != 'End':
    if command == 'one':
        player_two_eggs -= 1
    elif command == 'two':
        player_one_eggs -= 1
    # else:
    #     print(f'Invalid command! You can only perform two commands: "one" or "two".')
    if player_one_eggs == 0:
        print(f'Player one is out of eggs. Player two has {player_two_eggs} eggs left.')
        break
    elif player_two_eggs == 0:
        print(f'Player two is out of eggs. Player one has {player_one_eggs} eggs left.')
        break
    command = input()

if command == 'End':
    print(f'Player one has {player_one_eggs} eggs left.')
    print(f'Player two has {player_two_eggs} eggs left.')