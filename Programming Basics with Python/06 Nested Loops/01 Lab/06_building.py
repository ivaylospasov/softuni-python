floors = int(input())
spaces = int(input())

space_number = ''

for floor in range(floors, 0, -1):
    for space in range(spaces):
        if floor == floors:
            space_number += f'L{floor}{space} '
        elif floor % 2 == 0:
            space_number += f'O{floor}{space} '
        else:
            space_number += f'A{floor}{space} '
    print(space_number)
    space_number = ''
