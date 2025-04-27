BREAK_COMMAND = 'Christmas'
TOY_PRICE = 5
SWEATER_PRICE = 15

adult_count = 0
kids_count = 0
toys_cost = 0
sweaters_cost = 0


while True:
    family_member_age = input()

    if family_member_age == BREAK_COMMAND:
        break
    elif int(family_member_age) <= 16:
        kids_count += 1
        toys_cost += TOY_PRICE
    else:
        adult_count += 1
        sweaters_cost += SWEATER_PRICE

print(f'Number of adults: {adult_count}')
print(f'Number of kids: {kids_count}')
print(f'Money for toys: {toys_cost}')
print(f'Money for sweaters: {sweaters_cost}')

