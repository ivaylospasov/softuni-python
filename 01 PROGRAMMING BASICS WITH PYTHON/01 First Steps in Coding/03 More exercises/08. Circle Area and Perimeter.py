from math import pi

r = float(input())
calculated_area = '{:.2f}'.format(round((pi * r * r), 2))
calculated_perimeter = '{:.2f}'.format(round((2 * pi * r), 2))

print(calculated_area)
print(calculated_perimeter)
