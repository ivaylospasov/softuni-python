numbers_as_string = input().split(', ')

for char in numbers_as_string:
    if char == '0':
        numbers_as_string.remove(char)
        numbers_as_string.append(char)

numbers_as_integers = []

for number in numbers_as_string:
    numbers_as_integers.append(int(number))

print(numbers_as_integers)
