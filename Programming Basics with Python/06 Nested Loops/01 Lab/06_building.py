floors = int(input())
spaces = int(input())

space_number = ''

while floors > 0:

    for floor in range(1, floors + 1):
        for space in range(0, spaces):
            print(f'{floor}{floor}{space}', end=' ')

    # else:
    #     for floor in range(1, floors):
    #         for space in range(0, spaces):
    #             print(f'{floor}{floor}{space}', end=' ')

    floors -= 1