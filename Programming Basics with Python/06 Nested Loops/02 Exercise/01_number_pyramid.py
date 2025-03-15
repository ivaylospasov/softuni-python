# Решена на курса през февруари 2025
n = int(input())

counter = 0
is_max_number = False

for row in range(1, n + 1):
    for col in range(row):
        counter += 1
        print(counter, end=" ")

        if counter == n:
            is_max_number = True
            break

    if is_max_number:
        break

    print() # prints an empty row in outer loop

# n = int(input())
# current = 1
# is_current_bigger_than_n = False
#
# for row in range(1, n + 1):
#     for col in range(1, row + 1):
#
#         if current > n:
#             is_current_bigger_than_n = True
#             break
#         print(str(current) + ' ', end='')
#         current += 1
#     if is_current_bigger_than_n:
#         break
#     print()