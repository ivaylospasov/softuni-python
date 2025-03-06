# TODO Да видя грешката по време на курса

import sys

min_number = sys.maxsize
max_number = -sys.maxsize

n = int(input())

for i in range(0, n):
    num = int(input())
    if num > max_number:
        max_number = num
    elif num < min_number:
        min_number = num

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
