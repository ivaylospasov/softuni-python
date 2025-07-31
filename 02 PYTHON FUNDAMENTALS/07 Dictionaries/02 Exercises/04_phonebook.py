phonebook = {}

# Read entries until we get a number
while True:
    entry = input()
    
    # Check if the entry is a number
    if entry.isdigit():
        # If it's a number, convert it to int and break the loop
        n = int(entry)
        break
    
    # Split the entry by "-" to get name and number
    if "-" in entry:
        name, number = entry.split("-")
        
        # Add or update the entry in the phonebook
        phonebook[name] = number
    else:
        # Skip malformed entries
        continue

# Process search queries
for _ in range(n):
    search_name = input()
    
    # Check if the name exists in the phonebook
    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")