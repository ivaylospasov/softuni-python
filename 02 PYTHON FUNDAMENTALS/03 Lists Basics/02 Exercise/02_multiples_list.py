factor = int(input())
count = int(input())

current_list = []

for i in range(1, count + 1):
    current_list.append(factor * i)

print(current_list)