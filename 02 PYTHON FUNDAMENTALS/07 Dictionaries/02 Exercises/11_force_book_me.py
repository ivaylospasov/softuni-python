force_book = {}
#  force_book = {"light": ["Pesho", "Gosho"], "dark": ["Dart Vader", "Chubaka"]}

command = input()

while True:
    if command == "Lumpawaroo":
        break

    if ' | ' in command:
        force_side, force_user = command.split(' | ')
        if force_user in force_book.values():
            command = input()
            continue

        # Трябва да се създаде списък.....
        elif (force_side not in force_book.keys() and force_user not in force_book.values() or
              force_side in force_book.keys() and force_user not in force_book.values()):
            force_book[force_side].append(force_user)

    elif ' -> ' in command:
        force_user, force_side = command.split(' -> ')
        for side, users in force_book.items():
            if force_user in users:
                force_book[side].remove(force_user)
                force_book[force_side] = [force_user]
                print(f"{force_user} joins the {force_side} side!")
                break
            else:
                force_book[force_side] = force_user

    command = input()

print(force_book)