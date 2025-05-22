numbers_as_string = input().split(' ')
current_string = input()

search_indexes = []
sum_of_digits = 0

print(numbers_as_string)

for number_string in numbers_as_string:
    for digit_index in range(0, len(number_string)):
        sum_of_digits += int(number_string[digit_index])
    search_indexes.append(sum_of_digits)
    sum_of_digits = 0

print(search_indexes)

print(len(current_string))

reversed_string = current_string[::-1]

for index in search_indexes:
    if index > len(reversed_string):
        print(reversed_string[(len(reversed_string)-1) - search_indexes[index]], sep='')
    else:
        print(reversed_string[search_indexes[index]])