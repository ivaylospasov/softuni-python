current_list = input().split()
negative_list = []

for current_value in current_list:
    new_value = -int(current_value)
    negative_list.append(new_value)

print(negative_list)