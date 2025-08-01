key_fragments = {
    "shards": [0, "Shadowmourne"],
    "fragments": [0, "Valanyr"],
    "motes": [0, "Dragonwrath"]
}

legendary_item_obtained = False

while not legendary_item_obtained:

    items = input().lower().split()

    fragments = items[1::2]
    quantity = items[::2]

    for fragment, quantity in zip(fragments, quantity):

        if fragment in key_fragments.keys():
            key_fragments[fragment][0] += int(quantity)

            if key_fragments["shards"][0] >= 250:
                print(f'{key_fragments["shards"][1]} obtained!')
                key_fragments["shards"][0] -= 250
                legendary_item_obtained = True
                break
            elif key_fragments["fragments"][0] >= 250:
                print(f'{key_fragments["fragments"][1]} obtained!')
                key_fragments["fragments"][0] -= 250
                legendary_item_obtained = True
                break
            elif key_fragments["motes"][0] >= 250:
                print(f'{key_fragments["motes"][1]} obtained!')
                key_fragments["motes"][0] -= 250
                legendary_item_obtained = True
                break

        else:
            key_fragments[fragment] = [int(quantity)]

for key, value in key_fragments.items():
    print(f'{key}: {value[0]}')
