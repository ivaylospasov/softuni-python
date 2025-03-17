from icecream import ic

number = input()
# number_two = int(input())
sum_odd_numbers = 0
sum_even_numbers = 0
list_results = []

# for number in range(number_one + 1, number_two):
#     number_string = str(number)
for index in range(len(number)):
    if (index+1) % 2 != 0:
        sum_odd_numbers += int(number[index])
        print(number[index], end=' ')
    else:
        sum_even_numbers += int(number[index])
        print(number[index], end=' ')

print()
ic(sum_odd_numbers)
ic(sum_even_numbers)