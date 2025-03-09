import sys

max_number = -sys.maxsize

data = ''

while True:
    data = input()
    if data != 'Stop':
        data = int(data)
        if data > max_number:
            max_number = data
    else:
        print(f'{max_number}')
        break
