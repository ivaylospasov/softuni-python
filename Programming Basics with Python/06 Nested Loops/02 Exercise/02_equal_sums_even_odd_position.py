number_one = int(input())
number_two = int(input())
sum_odd_numbers = 0
sum_even_numbers = 0

for number in range(number_one, number_two):
    number_string = str(number)
    for index in range(len(number_string)):
        if int(number_string[index]) % 2 != 0:
            sum_odd_numbers += int(number_string[index])
        else:
            sum_even_numbers += int(number_string[index])
    if sum_odd_numbers == sum_even_numbers:
        print(number_string)
