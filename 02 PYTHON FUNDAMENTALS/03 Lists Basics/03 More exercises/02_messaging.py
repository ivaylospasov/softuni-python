numbers_as_strings = input().split(' ')
current_string = input()
message = ''

search_indexes = []
sum_of_digits = 0

for number_string in numbers_as_strings:
    for digit_index in range(0, len(number_string)):
        sum_of_digits += int(number_string[digit_index])
    search_indexes.append(sum_of_digits)
    sum_of_digits = 0

string_length = len(current_string)
string_last_index = string_length - 1

for index in search_indexes:
    if index > string_last_index:
        char_to_message: str = current_string[index % string_length]
        message += char_to_message
        current_string = current_string.replace(char_to_message, '', 1)
    else:
        char_to_message: str = current_string[index]
        message += char_to_message
        current_string = current_string.replace(char_to_message, '', 1)

print(message)