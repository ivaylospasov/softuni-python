number = int(input())

if abs(number) <= 100 and number != 0:
    print('Yes')
else:
    print('No')

# Алтернативно с NOT
#
# if abs(number) <= 100 and not number == 0:
#     print('Yes')
# else:
#     print('No')