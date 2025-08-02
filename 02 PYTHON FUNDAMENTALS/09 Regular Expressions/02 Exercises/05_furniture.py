import re

bought_furniture = []
total_cost = 0

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

command = input()

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        # print(match.groups())
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)

    command = input()

print('Bought furniture:')
for item in bought_furniture:
    print(item)
print(f'Total money spend: {total_cost:.2f}')