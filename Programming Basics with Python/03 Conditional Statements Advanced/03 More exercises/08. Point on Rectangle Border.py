x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if ((x == x1 and y1 <= y <= y2) or
        (x == x2 and y1 <= y <= y2) or
        (y == y1 and x1 <= x <= x2) or
        (y == y2 and x1 <= x <= x2)):
    output = 'Border'
else:
    output = 'Inside / Outside'

print(output)