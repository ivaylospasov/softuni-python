pairs = int(input())

max_diff = 0
previous_pair_sum = 0

for i in range(1, pairs + 1):
    fist_number = int(input())
    second_number = int(input())
    if i == 1:
        previous_pair_sum = fist_number + second_number
    else:
        next_pair_sum = fist_number + second_number
        if next_pair_sum != previous_pair_sum:
            diff = abs(next_pair_sum - previous_pair_sum)
            if diff > max_diff:
                max_diff = diff
            previous_pair_sum = next_pair_sum

if max_diff != 0:
    print(f'No, maxdiff={max_diff}')
else:
    print(f'Yes, value={previous_pair_sum}')
