# Read the initial number of eggs for each player
player_one_eggs = int(input())
player_two_eggs = int(input())

# Game loop
while player_one_eggs > 0 and player_two_eggs > 0:
    command = input()
    
    # Check if the game should end
    if command == "End":
        break
    
    # Process the commands
    if command == "one":
        player_two_eggs -= 1
    elif command == "two":
        player_one_eggs -= 1

# Output the result
if player_one_eggs <= 0:
    print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
elif player_two_eggs <= 0:
    print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
else:
    print(f"Player one has {player_one_eggs} eggs left.")
    print(f"Player two has {player_two_eggs} eggs left.")