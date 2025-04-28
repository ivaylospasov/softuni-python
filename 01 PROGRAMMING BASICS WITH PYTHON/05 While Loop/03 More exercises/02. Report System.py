charity_sum_expected = int(input())
current_charity_sum = 0

current_charity_sum_cash = 0
current_charity_sum_card = 0

transaction_tries = 0
transaction_count_cash = 0
transaction_count_card = 0

average_cash_charity = 0
average_card_charity = 0

while current_charity_sum < charity_sum_expected:
    current_sum = input()

    if current_sum == "End":
        print("Failed to collect required money for charity.")
        break

    current_sum = int(current_sum)
    transaction_tries += 1

    if transaction_tries % 2 != 0:
        if current_sum > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            current_charity_sum_cash += current_sum
            current_charity_sum += current_sum
            transaction_count_cash += 1
    else:
        if current_sum < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            current_charity_sum_card += current_sum
            current_charity_sum += current_sum
            transaction_count_card += 1


if current_charity_sum >= charity_sum_expected:
    if transaction_count_cash > 0:
        average_cash_charity = current_charity_sum_cash / transaction_count_cash

    if transaction_count_card > 0:
        average_card_charity = current_charity_sum_card / transaction_count_card

    print(f"Average CS: {average_cash_charity:.2f}")
    print(f"Average CC: {average_card_charity:.2f}")
