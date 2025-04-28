base_a = float(input())
base_b = float(input())
height = float(input())

# trapezoid_area = '{:.2f}'.format(round(((base_a + base_b) * height/2), 2))
# trapezoid_area = '{:.2f}'.format(((base_a + base_b) * height/2))
trapezoid_area = (base_a + base_b) * height / 2

print(f'{trapezoid_area:.2f}')