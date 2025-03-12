destination = input()

while destination != "End":

    budget = float(input())

    while budget > 0:
        saved_money = float(input())
        budget -= saved_money

    print(f"Going to {destination}!")
    
    destination = input()
