initial_energy = 100
initial_coins = 100

events = input().split("|")
events_handled = 0

events_elements_as_list = []

for element in events:
    events_elements_as_list.append(element.split("-"))

for event in events_elements_as_list:
    if event[0] == "rest":
        energy_change = int(event[1])
        initial_energy += energy_change
        if initial_energy > 100:
            initial_energy = 100
            energy_change = 0
            print(f'You gained {energy_change} energy.')
        else:
            print(f'You gained {energy_change} energy.')
        print(f"Current energy: {initial_energy}.")
        events_handled += 1
    elif event[0] == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            coins_change = int(event[1])
            initial_coins += coins_change
            print(f'You earned {coins_change} coins.')
            events_handled += 1
        else:
            initial_energy += 50
            print(f'You had to rest!')
    else:
        ingredient = event[0]
        ingredient_price = int(event[1])
        if initial_coins >= ingredient_price:
            initial_coins -= ingredient_price
            print(f'You bought {ingredient}.')
            events_handled += 1
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            break


if events_handled == len(events_elements_as_list):
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
