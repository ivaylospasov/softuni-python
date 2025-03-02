x = float(input())
y = float(input())
h = float(input())

# Боядисана площ с 1 литър боя
green_paint_area_by_litter = 3.4
red_paint_area_by_litter = 4.3

# Вратата е правоъгълник
front_door_widht = 1.2
front_door_height = 2
front_door_area = front_door_widht * front_door_height

# Предна и задна стена - квадрати с площ (минус вратата)
front_and_back_walls_area = 2 * (x * x) - front_door_area

# Страничният прозорец е квадрат
# Има по един на всяка странична стена
side_window_width = 1.5
side_window_area = side_window_width * side_window_width

side_walls_area = 2 * (x * y) - (2 * side_window_area)

walls_area = front_and_back_walls_area + side_walls_area

# Покрив
# Два странични правоъгълника със следните лица
roof_sides_area = 2 * (x * y)

# Два триъгълника със следните лица
roof_triangles_area = 2 * ((x * h) / 2)

roof_area = roof_sides_area + roof_triangles_area

green_paint_litres = '{:.2f}'.format(round((walls_area / green_paint_area_by_litter), 2))
red_paint = '{:.2f}'.format(round((roof_area / red_paint_area_by_litter), 2))

print(green_paint_litres)
print(red_paint)
