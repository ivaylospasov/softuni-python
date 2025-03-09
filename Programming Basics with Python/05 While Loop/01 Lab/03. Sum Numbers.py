number = int(input())

sum_of_numbers = 0

while sum_of_numbers < number:
    current_number = int(input())
    sum_of_numbers += current_number

print(sum_of_numbers)

# Алтернативно

# while True:
#     current_number = int(input())
#     sum_of_numbers += current_number
#
#     if sum_of_numbers >= number:
#         print(sum_of_numbers)
#         break


