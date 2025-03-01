annual_fee = int(input())

snickers = annual_fee - (0.4 * annual_fee)
basketball_clothes = snickers - (0.2 * snickers)
basketball = 0.25 * basketball_clothes
accessories = 0.2 * basketball

separate_costs_list = [annual_fee, snickers, basketball_clothes, basketball, accessories]
total_cost_per_year = sum(separate_costs_list)

print(total_cost_per_year)