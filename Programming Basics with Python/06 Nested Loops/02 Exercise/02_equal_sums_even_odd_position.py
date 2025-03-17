from icecream import ic

number_one = int(input())
number_two = int(input())
sum_odd_numbers = 0
sum_even_numbers = 0
list_results = []

for number in range(number_one + 1, number_two):
    number_string = str(number)
    for index in range(len(number_string)):
        if (index+1) % 2 != 0:
            sum_odd_numbers += int(number_string[index])
            # ic(sum_odd_numbers)
        else:
            sum_even_numbers += int(number_string[index])
            # ic(sum_even_numbers)
    if sum_odd_numbers == sum_even_numbers:
        # print(number_string + ' ', end=' ')
        list_results.append(number_string)
        sum_odd_numbers = 0
        sum_even_numbers = 0

ic(list_results)