current_word = input()
stop_command = "End"

while current_word != stop_command:
    if current_word == 'SoftUni':
        pass
    else:
        for char in current_word:
            double_char = char * 2
            print(f"{double_char}", end="")
        print()
    current_word = input()