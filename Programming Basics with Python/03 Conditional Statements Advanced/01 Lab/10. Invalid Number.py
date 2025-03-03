number = int(input())

if 100 <= number <= 200 or number == 0:
    pass
else:
    print('invalid')

# От учебника

number = int(input())

in_range = (number >= 100 and number <= 200) or number == 0
if not in_range:
    print('invalid')