nylon_prise = 1.5
paint_prise = 14.5
paint_thinner_prise = 5
bags_prise = 0.4

nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
working_hours = int(input())

paint_quantity = paint_quantity * 1.1
# print(f'Paint quantity: {paint_quantity}')

nylon_quantity = nylon_quantity + 2
# print(f'Nylon quantity: {nylon_quantity}')

nylon_total_cost = nylon_quantity * nylon_prise
# print(f'Nylon total price: {nylon_total_cost}')

paint_total_cost = paint_quantity * paint_prise
# print(f'Paint total price: {paint_total_cost}')

paint_thinner_total_cost = paint_thinner_quantity * paint_thinner_prise
# print(f'Paint thinner total price: {paint_thinner_total_cost}')

all_prises = [nylon_total_cost, paint_total_cost, paint_thinner_total_cost, bags_prise]
materials_total_cost = sum(all_prises)
# print(f'Materials total cost: {materials_total_cost}')

work_per_hour_prise = 0.3 * materials_total_cost
work_total_cost = work_per_hour_prise * working_hours
# print(f'Work total cost: {work_total_cost}')

total_cost = materials_total_cost + work_total_cost
print(total_cost)