gifts = input().split()
command = input().split(sep=' ')

STOP_COMMAND = "No Money".split(sep=' ')

while command != STOP_COMMAND:
    if command[0] == "OutOfStock" and command[1] in gifts:
        for gift in gifts[::-1]:
            if gift == command[1]:
                gifts[gifts.index(gift)] = "None"

    elif command[0] == "Required":
        gift_index = int(command[2])
        if abs(gift_index) < len(gifts):
            gifts[gift_index] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input().split(sep=' ')

if "None" in gifts:
    for gift in gifts[::-1]:
        if gift == "None":
            gifts.remove(gift)

print(' '.join(gifts))