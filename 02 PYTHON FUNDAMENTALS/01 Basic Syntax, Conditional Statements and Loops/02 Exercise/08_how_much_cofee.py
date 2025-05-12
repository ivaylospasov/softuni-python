event = input()
coffee_count = 0
stop_command = 'END'
event_list_lowercase = ['coding', 'cat', 'dog', 'movie']
event_list_uppercase = ['CODING', 'CAT', 'DOG', 'MOVIE']

while event != stop_command:
    if event in event_list_lowercase:
        coffee_count += 1
    elif event in event_list_uppercase:
        coffee_count += 2
    else:
        pass

    event = input()

if coffee_count <= 5:
    print(coffee_count)
else:
    print('You need extra sleep')