skumria_cost = float(input())
caca_cost = float(input())
palamud_weight = float(input())
safrid_weight = float(input())
midi_weight = int(input())

palamud_prise = 1.6 * skumria_cost
safrid_prise = 1.8 * caca_cost
midi_prise = 7.5

palamud_cost = palamud_prise * palamud_weight
safrid_cost = safrid_prise * safrid_weight
midi_cost = midi_prise * midi_weight

all_costs = [palamud_cost, safrid_cost, midi_cost]
total_cost = '{:.2f}'.format(round(sum(all_costs), 2))

print(total_cost)