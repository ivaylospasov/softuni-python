pack_of_pens_prise = 5.80
pack_of_markers_prise = 7.20
cleaning_agent_per_litter_prise = 1.20

packs_of_pens = int(input())
packs_of_markers = int(input())
cleaning_agent_litters = int(input())
discount_factor = int(input()) / 100

pens_amount = pack_of_pens_prise * packs_of_pens
markers_amount = pack_of_markers_prise * packs_of_markers
agent_amount = cleaning_agent_per_litter_prise * cleaning_agent_litters

all_amounts = [pens_amount, markers_amount, agent_amount]
total_amount = sum(all_amounts)

total_amount_discounted = total_amount - (total_amount * discount_factor)

print(total_amount_discounted)