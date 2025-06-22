sequence = input().split()

def absolute_values(list_of_numbers):
    for i in range(len(list_of_numbers)):
        list_of_numbers[i] = abs(float(list_of_numbers[i]))
    return list_of_numbers
    # return [abs(float(x)) for x in list_of_numbers] # alternative solution

print(absolute_values(sequence))