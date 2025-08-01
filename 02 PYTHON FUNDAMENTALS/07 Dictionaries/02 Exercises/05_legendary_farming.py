#"Shadowmourne" - requires 250 Shards
#"Valanyr" - requires 250 Fragments
#"Dragonwrath" - requires 250 Motes

key_fragments = {
    "Shards": 0,
    "Fragments": 0,
    "Motes": 0
}

items_list = []
items_quantity = []


# while key_fragments["Shards"] < 250 \
#         or key_fragments["Fragments"] < 250 \
#         or key_fragments["Motes"] < 250:
#     items = input().split()

items = input().split()

fragments = items[1::2]
quantity = items[::2]

for index, fragment in enumerate(fragments):
    if fragments[index] not in key_fragments.keys():
        key_fragments[fragments[index]] = int(quantity[index])
    else:
        key_fragments[fragments[index]] += int(quantity[index])


print(fragments)
print(quantity)
print(key_fragments)
