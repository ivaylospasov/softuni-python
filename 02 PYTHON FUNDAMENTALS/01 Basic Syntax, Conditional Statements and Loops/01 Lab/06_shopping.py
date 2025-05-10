budget = float(input())
total_cost = 0
stop_shopping_command = 'End'

while True:
    command = input()
    if command == stop_shopping_command:
        break
    current_product_price = int(command)
    total_cost += current_product_price
    if total_cost > budget:
        print('You went in overdraft!')
        break

if total_cost <= budget:
    print('You bought everything needed.')

# Alternative solution
# command = input()
# while command != 'End':
#     current_product_price = int(command)
#     budget -= current_product_price
#     if budget < 0:
#         print('You went in overdraft!')
#         break
#     command = input()
# else:
#     print('You bought everything needed.')



