stadium_capacity = int(input())
total_fans = int(input())

fans_in_sector_a = 0
fans_in_sector_b = 0
fans_in_sector_v = 0
fans_in_sector_g = 0

for fan in range(1, total_fans + 1):
    sector = input().lower()
    if sector == 'a':
        fans_in_sector_a += 1
    elif sector == 'b':
        fans_in_sector_b += 1
    elif sector == 'v':
        fans_in_sector_v += 1
    else:
        fans_in_sector_g += 1

fans_in_sector_a_percentage = fans_in_sector_a / total_fans * 100
fans_in_sector_b_percentage = fans_in_sector_b / total_fans * 100
fans_in_sector_v_percentage = fans_in_sector_v / total_fans * 100
fans_in_sector_g_percentage = fans_in_sector_g / total_fans * 100
fans_percentage = total_fans / stadium_capacity * 100

print(f'{fans_in_sector_a_percentage:.2f}%')
print(f'{fans_in_sector_b_percentage:.2f}%')
print(f'{fans_in_sector_v_percentage:.2f}%')
print(f'{fans_in_sector_g_percentage:.2f}%')
print(f'{fans_percentage:.2f}%')
