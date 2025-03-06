# Важно е да се знае, че има 2 if-а, а не elif

import sys

min_number = sys.maxsize
max_number = -sys.maxsize

n = int(input())

for i in range(0, n):
    num = int(input())
    if num > max_number:
        max_number = num
        # print(f'Current Max number is {max_number}')
    if num < min_number:
        min_number = num
        # print(f'Current Min number is {min_number}')

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
