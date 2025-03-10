change = float(input())

leva_2 = 0
leva_1 = 0
coins_50 = 0
coins_20 = 0
coins_10 = 0
coins_05 = 0
coins_02 = 0
coins_01 = 0

change_left = 0
coins_counter: int = 0

change_in_coins: float = change * 100


if change_in_coins >= 200:
    leva_2 = change_in_coins // 200
    coins_counter += leva_2
    change_in_coins = change_in_coins - (leva_2 * 200)

if 100 <= change_in_coins < 200:
    leva_1 = change_in_coins // 100
    coins_counter += leva_1
    change_in_coins = change_in_coins - (leva_1 * 100)

if 50 <= change_in_coins < 100:
    coins_50 = 1
    coins_counter += coins_50
    change_in_coins = change_in_coins - (coins_50 * 50)

if 20 <= change_in_coins < 50:
    coins_20 = change_in_coins // 20
    coins_counter += coins_20
    change_in_coins = change_in_coins - (coins_20 * 20)

if 10 <= change_in_coins < 20:
    coins_10 = change_in_coins // 10
    coins_counter += coins_10
    change_in_coins = change_in_coins - (coins_10 * 10)

if 5 <= change_in_coins < 10:
    coins_05 = change_in_coins // 5
    coins_counter += coins_05
    change_in_coins = change_in_coins - (coins_05 * 5)

if 2 < change_in_coins < 5:
    coins_02 = change_in_coins // 2
    coins_counter += coins_02
    change_in_coins = change_in_coins - (coins_02 * 2)

if 1 <= change_in_coins < 2:
    coins_01 = 1
    coins_counter += 1
    change_in_coins = change_in_coins - coins_01

print(int(coins_counter))