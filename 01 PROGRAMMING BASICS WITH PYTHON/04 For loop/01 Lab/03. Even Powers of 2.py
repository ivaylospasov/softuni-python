# n = int(input())
#
# for i in range(0, n+1):
#     if i % 2 == 0:
#         print(2 ** i)

# Решение на презентацията

n = int(input())

num = 1

for i in range(0, n + 1, 2):
    print(num)
    num = num * 2 * 2