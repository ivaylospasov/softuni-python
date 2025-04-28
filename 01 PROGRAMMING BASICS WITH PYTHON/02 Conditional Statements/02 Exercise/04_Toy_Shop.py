vacation_prise = float(input())

puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

puzzle_prise = 2.6
doll_prise = 3
bear_prise = 4.1
minion_prise = 8.2
truck_prise = 2

puzzles_profit = puzzles_number * puzzle_prise
dolls_profit = dolls_number * doll_prise
bears_profit = bears_number * bear_prise
minions_profit = minions_number * minion_prise
trucks_profit = trucks_number * truck_prise

all_toys = sum([puzzles_number, dolls_number, bears_number, minions_number, trucks_number])
total_profit = sum([puzzles_profit, dolls_profit, bears_profit, minions_profit, trucks_profit])

if all_toys >= 50:
    total_profit -= 0.25 * total_profit

rent = 0.1 * total_profit
money_left = total_profit - rent

if money_left >= vacation_prise:
    money_left -= vacation_prise
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = vacation_prise - money_left
    print(f'Not enough money! {money_needed:.2f} lv needed.')
