first_number = int(input())
second_number = int(input())
third_number = int(input())

# Shortest way
# print(max(first_number, second_number, third_number))

max_number = first_number

if second_number > max_number:
    max_number = second_number

if third_number > max_number:
        max_number = third_number

print(max_number)