number = int(input())

for i in range(1, number + 1):
    print(i * "*")

for i in range(number - 1, 0, -1):
    print(i * "*")

# Alternative solution
# for i in range(1, number + 1):
#     for j in range(0, i):
#         print("*", end="")
#     print() # new line
#
# for i in range(number - 1, 0, -1):
#     for j in range(0, i):
#         print("*", end="")
#     print()