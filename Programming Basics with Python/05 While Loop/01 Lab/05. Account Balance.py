available_sum = 0

while True:
    data = input()

    if data == 'NoMoreMoney':
        print(f'Total: {available_sum:.2f}')
        break

    current_sum = float(data)

    if current_sum >= 0:
        available_sum += current_sum
        print(f'Increase: {current_sum:.2f}')
    else:
        print('Invalid operation!')
        print(f'Total: {available_sum:.2f}')
        break