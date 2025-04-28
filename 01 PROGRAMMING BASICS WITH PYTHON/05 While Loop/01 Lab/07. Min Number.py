import sys

min_number = sys.maxsize

data = ''

while True:
    data = input()
    if data != 'Stop':
        data = int(data)
        if data < min_number:
            min_number = data
    else:
        print(f'{min_number}')
        break
