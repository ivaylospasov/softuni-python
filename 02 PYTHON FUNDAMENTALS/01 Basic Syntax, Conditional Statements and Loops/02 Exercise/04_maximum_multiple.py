divisor = int(input())
boundary = int(input())

# Set the range in reversed order to get the largest number

for i in range(boundary, 0, -1):
    if i % divisor == 0:
        print(i)
        break

