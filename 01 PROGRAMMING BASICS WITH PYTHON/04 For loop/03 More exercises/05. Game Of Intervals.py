turns = int(input())

numbers_from_0_to_9 = 0
numbers_from_10_19 = 0
numbers_from_20_29 = 0
numbers_from_30_39 = 0
numbers_from_40_50 = 0
invalid_numbers = 0
result = 0

for turn in range(1, turns + 1):
    num = int(input())
    if 0 <= num <= 9:
        result += 0.2 * num
        numbers_from_0_to_9 += 1
    elif 10 <= num <= 19:
        result += 0.3 * num
        numbers_from_10_19 += 1
    elif 20 <= num <= 29:
        result += 0.4 * num
        numbers_from_20_29 += 1
    elif 30 <= num <= 39:
        result += 50
        numbers_from_30_39 += 1
    elif 40 <= num <= 50:
        result += 100
        numbers_from_40_50 += 1
    else:
        invalid_numbers += 1
        result = result / 2

print(f'{result:.2f}')
print(f'From 0 to 9: {(numbers_from_0_to_9 / turns * 100):.2f}%')
print(f'From 10 to 19: {(numbers_from_10_19 / turns * 100):.2f}%')
print(f'From 20 to 29: {(numbers_from_20_29 / turns * 100):.2f}%')
print(f'From 30 to 39: {(numbers_from_30_39 / turns * 100):.2f}%')
print(f'From 40 to 50: {(numbers_from_40_50 / turns * 100):.2f}%')
print(f'Invalid numbers: {(invalid_numbers / turns * 100):.2f}%')
