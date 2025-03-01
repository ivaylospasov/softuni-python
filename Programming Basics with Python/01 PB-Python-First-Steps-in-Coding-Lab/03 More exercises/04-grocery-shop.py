vegetables_prise = float(input('Enter the prise of 1 kg vegetables in leva: '))
fruits_prise = float(input('Enter the prise of of 1 kg fruits in leva: '))

vegetables_weight = int(input('Enter the weight of vegetables in kg: '))
fruits_weight = int(input('Enter the weight of fruits in kg: '))

cost_vegetables = vegetables_weight * vegetables_prise
cost_fruits = fruits_weight * fruits_prise

total_cost_leva =  cost_vegetables + cost_fruits
total_cost_euro = '{:.2f}'.format(round(total_cost_leva / 1.94, 2))

print(total_cost_euro)
