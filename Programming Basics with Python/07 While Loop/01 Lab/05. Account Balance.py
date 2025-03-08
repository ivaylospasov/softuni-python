transaction_count = int(input())

# TODO Да гледам във видеото

balance = 0

while True:
    add_sum = float(input())
    if add_sum >= 0:
        balance += add_sum
        transaction_count -= 1
    else:
        print("Invalid operation")
        print("Balance: ", balance)
        break

    if transaction_count == 0:
        print("Balance: ", balance)
        break