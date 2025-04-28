# МОЕ РЕШЕНИЕ
#
# vacation_cost: float = float(input())
# current_money: float = float(input())
#
# action: str = input() # save or spend
# money_amount: float = float(input())
#
# spend_times: int = 0
# save_times: int = 0
#
# days_past: int = 0
#
# is_failed = False
#
# while current_money < vacation_cost:
#
#     if action == 'spend':
#         spend_times += 1
#         current_money -= money_amount
#         if current_money - money_amount < 0:
#             current_money = 0
#         days_past += 1
#
#     if spend_times >= 5:
#         is_failed = True
#         break
#
#     if action == 'save':
#         current_money += money_amount
#         spend_times = 0
#         days_past += 1
#
#     if current_money >= vacation_cost:
#         break
#
#     action: str = input()
#     money_amount: float = float(input())
#
# if is_failed:
#     print('You can\'t save the money.')
#     print(f'{days_past}')
# else:
#     print(f'You saved the money for {days_past} days.')

needed_money = float(input())
owned_money = float(input())

days_counter = 0
spending_counter = 0

while owned_money < needed_money and spending_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1

    if command == 'save':
        owned_money += money
        spending_counter = 0
    elif command == 'spend':
        owned_money -= money
        spending_counter += 1
        if owned_money < 0:
            owned_money = 0

if spending_counter == 5:
    print('You can\'t save the money.')
    print(days_counter)

if owned_money >= needed_money:
    print(f'You saved the money for {days_counter} days.')