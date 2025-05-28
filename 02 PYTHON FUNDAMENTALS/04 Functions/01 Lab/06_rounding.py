string_of_numbers = input().split(' ')

print([round(float(x)) for x in string_of_numbers])

# for index in range(len(string_of_numbers)):
#     string_of_numbers[index] = round(float(string_of_numbers[index]))
#
# print(string_of_numbers)