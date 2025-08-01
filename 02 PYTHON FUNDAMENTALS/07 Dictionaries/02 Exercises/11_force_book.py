force_sides = {}  # Dictionary to store force sides and their users

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if " | " in command:
        # Format: "{force_side} | {force_user}"
        force_side, force_user = command.split(" | ")

        # Check if the user already exists in any side
        user_exists = False
        for side, users in force_sides.items():
            if force_user in users:
                user_exists = True
                break

        if not user_exists:
            # Add user to the side (create side if it doesn't exist)
            if force_side not in force_sides:
                force_sides[force_side] = []
            force_sides[force_side].append(force_user)

    elif " -> " in command:
        # Format: "{force_user} -> {force_side}"
        force_user, force_side = command.split(" -> ")

        # Remove user from current side if they exist
        for side, users in list(force_sides.items()):
            if force_user in users:
                users.remove(force_user)
                # Remove the side if it becomes empty
                if not users:
                    del force_sides[side]
                break

        # Add user to the new side (create side if it doesn't exist)
        if force_side not in force_sides:
            force_sides[force_side] = []
        force_sides[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

# Print the results
for force_side, users in force_sides.items():
    if users:  # Only print sides with at least one user
        print(f"Side: {force_side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
