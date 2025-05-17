n = int(input())
all_numbers_list = []
filtered_list = []
stop_command_list = ['even', 'odd', 'negative', 'positive']

for i in range(n):
    current_number = int(input())
    all_numbers_list.append(current_number)

command = input()

if command in stop_command_list:
    if command == 'even':
        filtered_list = [x for x in all_numbers_list if x % 2 == 0]
    elif command == 'odd':
        filtered_list = [x for x in all_numbers_list if x % 2 != 0]
    elif command == 'negative':
        filtered_list = [x for x in all_numbers_list if x < 0]
    elif command == 'positive':
        filtered_list = [x for x in all_numbers_list if x >= 0]

print(filtered_list)

# Alternative
# if command == 'even':
#     for number in all_numbers_list:
#         if number % 2 == 0:
#             filtered_list.append(number)
# elif command == 'odd':
#     for number in all_numbers_list:
#         if number % 2 != 0:
#             filtered_list.append(number)
# elif command == 'negative':
#     for number in all_numbers_list:
#         if number < 0:
# elif command == 'positive':
#     for number in all_numbers_list:
#         if number >= 0:
#             filtered_list.append(number)
#
# print(filtered_list)