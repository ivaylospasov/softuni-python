energy = 100
max_energy = 100
coins = 100

events = input().split("|")
events_handled = 0

events_elements_as_list = []

for element in events:
    events_elements_as_list.append(element.split("-"))

for event in events_elements_as_list:
    if event[0] == "rest":
        energy_change = int(event[1])
        if energy + energy_change > max_energy:
            energy_change = max_energy - energy
            energy = max_energy
        else:
            energy += energy_change
        print(f'You gained {energy_change} energy.')
        print(f"Current energy: {energy}.")
        events_handled += 1
    elif event[0] == "order":
        if energy >= 30:
            energy -= 30
            coins_change = int(event[1])
            coins += coins_change
            events_handled += 1
            print(f'You earned {coins_change} coins.')
        else:
            energy += 50
            if energy > max_energy:
                energy = max_energy
            print(f'You had to rest!')
    else:
        ingredient = event[0]
        ingredient_price = int(event[1])
        if coins >= ingredient_price:
            coins -= ingredient_price
            print(f'You bought {ingredient}.')
            events_handled += 1
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            break


if events_handled == len(events_elements_as_list):
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

# TODO Correct the code!