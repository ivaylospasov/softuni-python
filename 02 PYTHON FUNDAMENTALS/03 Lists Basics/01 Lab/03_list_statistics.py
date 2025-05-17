n = int(input())

list_of_positive_numbers = []
list_of_negative_numbers = []

for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        list_of_positive_numbers.append(current_number)
    elif current_number < 0:
        list_of_negative_numbers.append(current_number)
    else:
        pass

positive_numbers_count = len(list_of_positive_numbers)
negative_numbers_sum = sum(list_of_negative_numbers)

print(list_of_positive_numbers)
print(list_of_negative_numbers)
print(f'Count of positives: {positive_numbers_count}')
print(f'Sum of negatives: {negative_numbers_sum}')