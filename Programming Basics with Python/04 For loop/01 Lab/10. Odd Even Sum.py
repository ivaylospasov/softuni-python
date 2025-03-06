n = int(input())

odd_index_sum = 0
even_index_sum = 0


for i in range(1, n + 1):
    number = int(input())
    if i % 2 == 0:
        even_index_sum += number
    else:
        odd_index_sum += number

diff = abs(odd_index_sum - even_index_sum)

if odd_index_sum == even_index_sum:
    output_ln_one = 'Yes'
    output_ln_two = f'Sum = {odd_index_sum}'
else:
    output_ln_one = 'No'
    output_ln_two = f'Diff = {diff}'

print(output_ln_one)
print(output_ln_two)