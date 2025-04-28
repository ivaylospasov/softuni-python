deposit_start_amount = float(input())
deposit_period = int(input())
deposit_interest_percent = float(input())

deposit_interest = deposit_interest_percent / 100

deposit_end_amount = deposit_start_amount + deposit_period * ((deposit_start_amount * deposit_interest) / 12)

print(deposit_end_amount)