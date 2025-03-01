degrees_celsius = float(input('Enter the degrees celsius: '))

convert_to_fahrenheit = '{:.2f}'.format(round((degrees_celsius * 9 / 5) + 32, 2))

print(convert_to_fahrenheit)