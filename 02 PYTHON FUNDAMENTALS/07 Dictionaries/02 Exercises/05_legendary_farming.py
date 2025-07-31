#"Shadowmourne" - requires 250 Shards
#"Valanyr" - requires 250 Fragments
#"Dragonwrath" - requires 250 Motes

key_fragments = {
    "Shards": 0,
    "Fragments": 0,
    "Motes": 0
}

junk = {}

while key_fragments["Shards"] < 250 \
        or key_fragments["Fragments"] < 250 \
        or key_fragments["Motes"] < 250:
    items = input().split()
;
    for item in range(1, len(items) + 1, 2):
        if item not in key_fragments.keys():
            continue
        else:
            print(item)