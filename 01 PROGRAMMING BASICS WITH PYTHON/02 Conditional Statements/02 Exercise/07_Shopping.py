budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram_memory = int(input())

# %%
video_card_prise = 250
processor_prise = 0.35 * (number_video_cards * video_card_prise)
ram_memory_prise = 0.1 * (number_video_cards * video_card_prise)

# %%
video_cards_cost = number_video_cards * video_card_prise
processors_cost = number_processors * processor_prise
ram_memory_cost = number_ram_memory * ram_memory_prise

# %%
total_cost = sum([video_cards_cost, processors_cost, ram_memory_cost])

# %%
if number_video_cards > number_processors:
    total_cost -= 0.15 * total_cost

# %%
if budget >= total_cost:
    budget_left = budget - total_cost
    print(f'You have {budget_left:.2f} leva left!')
else:
    money_needed = total_cost - budget
    print(f'Not enough money! You need {money_needed:.2f} leva more!')