charity_sum_expected = int(input())
current_charity_sum = 0

current_charity_sum_cash = 0
current_charity_sum_card = 0

transaction_count = 0
transaction_count_cash = 0
transaction_count_card = 0

while current_charity_sum < charity_sum_expected:
    current_sum = input()
    if current_sum == "End":
        print("Failed to raise required money for charity.")
        break

    current_sum = float(current_sum)
    transaction_count += 1

    if transaction_count % 2 != 0:
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
    print(f"Average CS: {current_charity_sum_cash / transaction_count_cash}")
    print(f"Average CC: {current_charity_sum_card / transaction_count_card}")
