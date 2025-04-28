cake_width = int(input())
cake_length = int(input())

cake_size = cake_width * cake_length
cake_pieces = cake_size

take_pieces = input()

while cake_pieces >= 0:

    if take_pieces == "STOP":
        break
    else:
        take_pieces = int(take_pieces)

    cake_pieces -= take_pieces

    if cake_pieces <= 0:
        break

    take_pieces = input()

if cake_pieces < 0:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
else:
    print(f'{cake_pieces} pieces are left.')