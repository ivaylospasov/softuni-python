floors = int(input())
spaces = int(input())

space_number = ''

for floor in range(floors, 0, -1):
    for space in range(spaces):
        if floor == floors: # top floor
            space_number += f'L{floor}{space} '
        elif floor % 2 == 0: # even floor with offices
            space_number += f'O{floor}{space} '
        else: # odd floor with apartments
            space_number += f'A{floor}{space} '
    print(space_number)
    space_number = ''
