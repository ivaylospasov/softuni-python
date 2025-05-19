list_of_numbers_as_strings = input().split(sep=" ")
n = int(input())

list_of_numbers = []

for i in range(len(list_of_numbers_as_strings)):
    list_of_numbers.append(int(list_of_numbers_as_strings[i]))

sorted_list_of_numbers = list_of_numbers.copy()

sorted_list_of_numbers.sort(reverse=True)

sorted_list_of_numbers = sorted_list_of_numbers[-1:-n-1:-1]

for number in sorted_list_of_numbers:
    if number in list_of_numbers:
        list_of_numbers.remove(number)

list_of_numbers_as_strings.clear()

for number in list_of_numbers:
    list_of_numbers_as_strings.append(str(number))

print(', '.join(list_of_numbers_as_strings))
