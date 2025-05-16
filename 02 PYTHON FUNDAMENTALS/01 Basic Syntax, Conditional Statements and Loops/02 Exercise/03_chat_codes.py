n = int(input())

for _ in range(1, n + 1):
    number = int(input())
    if number == 88:
        current_message = "Hello"
    elif number == 86:
        current_message = "How are you?"
    elif number < 88: # Излишно е elif number !=86 and number !=88 and number < 88
        current_message = "GREAT!"
    else:
        current_message = "Bye."
    print(current_message)