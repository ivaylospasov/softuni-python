from math import floor, ceil

#%%
tennis_rocket_price = float(input())
tennis_rocket_count = int(input())
sneakers_count = int(input())

#%%
sneakers_price = round(tennis_rocket_price / 6, 2)
#%%
sneakers_cost = sneakers_count * sneakers_price

#%%
tennis_rockets_cost = tennis_rocket_count * tennis_rocket_price

#%%
total_cost_rockets_and_sneakers = sneakers_cost + tennis_rockets_cost

#%%

other_equipment_cost = round(total_cost_rockets_and_sneakers * 0.2, 2)


#%%
total_cost = total_cost_rockets_and_sneakers + other_equipment_cost

#%%
djokovich_paid = floor(total_cost / 8)

#%%
sponsors_paid = ceil(total_cost * 7/8)

#%%
print(f'Price to be paid by Djokovic {djokovich_paid}')
print(f'Price to be paid by sponsors {sponsors_paid}')
