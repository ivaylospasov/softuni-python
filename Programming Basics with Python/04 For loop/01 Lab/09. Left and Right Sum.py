n = int(input())

left_sum = 0
right_sum = 0

for i in range(0, n):
    input_number = int(input())
    left_sum += input_number

for i in range(0, n):
    input_number = int(input())
    right_sum += input_number

if left_sum == right_sum:
    output = f'Yes, sum = {left_sum}'
else:
    diff = abs(left_sum - right_sum)
    output = f'No, diff = {diff}'

print(output)
