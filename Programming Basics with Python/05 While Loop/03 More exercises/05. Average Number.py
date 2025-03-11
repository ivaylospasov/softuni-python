n = int(input())
numbers_sum = 0

for i in range(1, n+1):
    number = int(input())
    numbers_sum += number

average_number = numbers_sum / n
print(f'{average_number:.2f}')