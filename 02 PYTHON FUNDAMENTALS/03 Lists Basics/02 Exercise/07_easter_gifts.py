gifts = input().split()
command = input().split(sep=' ')

STOP_COMMAND = "No Money".split(sep=' ')

while command != STOP_COMMAND:
    if command[0] == "OutOfStock" and command[1] in gifts:
        for index in range(len(gifts)):
            if gifts[index] == command[1]:
                gifts[index] = "None"

    elif command[0] == "Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input().split(sep=' ')

if "None" in gifts:
    for gift in range(len(gifts) - 1, -1, -1):
        if gifts[gift] == "None":
            gifts.pop(gift)

print(' '.join(gifts))