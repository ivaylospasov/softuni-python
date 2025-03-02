vegetables_prise = float(input())
fruits_prise = float(input())

vegetables_weight = int(input())
fruits_weight = int(input())

cost_vegetables = vegetables_weight * vegetables_prise
cost_fruits = fruits_weight * fruits_prise

total_cost_leva =  cost_vegetables + cost_fruits
total_cost_euro = '{:.2f}'.format(round(total_cost_leva / 1.94, 2))

print(total_cost_euro)
