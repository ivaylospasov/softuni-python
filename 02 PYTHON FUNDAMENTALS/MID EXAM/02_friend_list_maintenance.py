friends_list = input().split(sep=', ')

END_COMMAND = 'Report'
REGULAR_COMMANDS = ['Blacklist', 'Error', 'Change']
STATUS_VALUES = ['Blacklisted', 'Lost']

def isvalid_index(idx):
    #valid_index = False
    if 0 <= int(idx) < len(friends_list):
        valid_index = True
        return valid_index
    return None

while True:
    command = input()

    if command == END_COMMAND:
        break

    command_parts = command.split(sep=' ')

    if command_parts[0] == REGULAR_COMMANDS[0]:
        friend_name = command_parts[1]
        if friend_name in friends_list:
            print(f'{friend_name} was blacklisted.')
            name_index = friends_list.index(friend_name)
            friends_list[name_index] = STATUS_VALUES[0]
        else:
            print(f'{friend_name} was not found.')

    elif command_parts[0] == REGULAR_COMMANDS[1]:
        search_index = int(command_parts[1])
        if isvalid_index(search_index) and friends_list[search_index] not in STATUS_VALUES:
            print(f'{friends_list[search_index]} was lost due to an error.')
            friends_list[search_index] = STATUS_VALUES[1]
        else:
            continue

    elif command_parts[0] == REGULAR_COMMANDS[2]:
        search_index = int(command_parts[1])
        new_name = command_parts[2]
        if isvalid_index(search_index):
            print(f'{friends_list[search_index]} changed his username to {new_name}.')
            friends_list[search_index] = new_name
        else:
            continue

final_list = ' '.join(friends_list)
blacklisted = friends_list.count(STATUS_VALUES[0])
lost = friends_list.count(STATUS_VALUES[1])

print(f'Blacklisted names: {blacklisted}')
print(f'Lost names: {lost}')
print(f'{final_list}')