string_of_numbers = input().split(sep=" ")
n = int(input())

print(string_of_numbers)

list_of_numbers = []

for i in range(len(string_of_numbers)):
    list_of_numbers.append(int(string_of_numbers[i]))

print(list_of_numbers)

list_of_numbers.sort(reverse=True)

print(list_of_numbers)