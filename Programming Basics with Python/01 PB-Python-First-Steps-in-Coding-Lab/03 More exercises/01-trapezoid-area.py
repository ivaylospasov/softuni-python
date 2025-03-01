base_a = float(input('Enter the base a size: '))
base_b = float(input('Enter the base b size: '))
height = float(input('Enter the height: '))

trapezoid_area = '{:.2f}'.format(round(((base_a + base_b) * height/2), 2))

print(trapezoid_area)