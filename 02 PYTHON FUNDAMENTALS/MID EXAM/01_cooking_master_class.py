from math import ceil

budget = float(input())
number_of_students = int(input())
flour_package_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())

# The educational set for one student consists of 1 package of flour, 10 eggs, and an apron.
EGGS_PER_STUDENT = 10

# You should know that the aprons get dirty often, so George should buy 20% more, rounded up to the next integer.
total_aprons = ceil(number_of_students * 1.2)

flour_total_cost = 0
eggs_total_cost = 0
apron_total_cost = 0

for student in range(1, number_of_students + 1):
    # Also, every fifth package of flour is free!!!!
    if student % 5 == 0:
        continue
    flour_total_cost += flour_package_price

for student in range(1, number_of_students + 1):
    eggs_total_cost += single_egg_price * EGGS_PER_STUDENT

apron_total_cost = total_aprons * single_apron_price

total_cost = flour_total_cost + apron_total_cost + eggs_total_cost

if total_cost <= budget:
    print(f'Items purchased for {total_cost:.2f}$.')
else:
    needed_money = abs(budget - total_cost)
    print(f'{needed_money:.2f}$ more needed.')