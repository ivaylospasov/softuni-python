number = int(input())
numbers_list = []


for i in range(1, number + 1):
    for digit in str(i):
        numbers_list.append(int(digit))
    if sum(numbers_list) == 5 or sum(numbers_list) == 7 or sum(numbers_list) == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
    numbers_list.clear()