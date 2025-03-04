x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

if (x == x1 and y1 <= y <= y2) or (x == x2 and y1 <= y <= y2) or (y == y1 and x1 <= x <= x2) or (y == y2 and x1 <= x <= x2):
    print('Border')

# TODO find outside and inside options