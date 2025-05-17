number_of_lines = int(input())
brackets_list = []
open_bracket_set = set()
close_bracket_set = set()

OPEN_BRACKET = '('
CLOSE_BRACKET = ')'

for string in range(1, number_of_lines + 1):
    current_string = input()
    if current_string == OPEN_BRACKET or current_string == CLOSE_BRACKET:
        brackets_list.append(current_string)

if len(brackets_list) % 2 == 0:

    for index in range(0, len(brackets_list), 2):
        open_bracket_set.add(brackets_list[index])
        close_bracket_set.add(brackets_list[index + 1])
    if open_bracket_set == {OPEN_BRACKET} and close_bracket_set == {CLOSE_BRACKET}:
        print("BALANCED")
    else:
        print("UNBALANCED")
else:
    print("UNBALANCED")