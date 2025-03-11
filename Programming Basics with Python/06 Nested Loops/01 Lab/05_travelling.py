destination = input()

while destination != "End":

    budget = float(input())

    while budget > 0:
        saved_money = float(input())
        budget -= saved_money

    print(f"Going to {destination}!")
    
    destination = input()

# 06. Nested Loops - Lab
# 05. Travelling
# You will be given a destination and budget. You need to calculate how much you need to save, in order to go to that
# destination.
# You will be given the destination and the needed budget. Afterwards you will be given the amount of money that you
# manage to save for a day, until you reach the needed budget.
# Keep in mind that you save money for a day, only if you have money left after you have subtracted the needed budget.
# If you don't have any money left after you have reached the needed budget, you won't save any money for a day.
# When you save enough money for the destination, print the following message: "Going to {destination}!" and read the
# next destination and budget.