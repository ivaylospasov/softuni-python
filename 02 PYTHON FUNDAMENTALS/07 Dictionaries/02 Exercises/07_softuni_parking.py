parking_data = {}

for action in range(int(input())):
    entry = input().split(' ')

    if len(entry) == 3: # This is registration to the parking
        username = entry[1]
        license_plate_number = entry[2]
        if username in parking_data.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking_data[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    else: # Someone is leaving the parking
        username = entry[1]
        if username in parking_data.keys():
            print(f"{username} unregistered successfully")
            parking_data.pop(username)
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate_number in parking_data.items():
    print(f"{username} => {license_plate_number}")