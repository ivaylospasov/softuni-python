gifts = input().split()
command = input().split()

stop_command = "No Money"

print(len(command))

while command != "No Money":
    if len(command) == 2:
        if command[0] == "OutOfStock":
            for gift in gifts[::-1]:
                if gift in gifts and gift == command[1]:
                    gifts[gifts.index(gift)] = "None"
        elif command[0] == "JustInCase":
            pass
    elif len(command) == 3:
        if command[0] == "Required":
            pass

    command = input()

# for gift_index in range(len(gifts) - 1, -1, -1):
#     if gifts[gift_index] == "None":
#         gifts.remove(gifts[gift_index])

for gift in gifts[::-1]:
    if gift == "None":
        gifts.remove(gift)

print(gifts)
