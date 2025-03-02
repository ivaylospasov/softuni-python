# %%
pool_volume = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
hours_missing = float(input())

# %%
all_pipes_debit = sum([pipe_one_debit, pipe_two_debit])
pipe_one_performance = pipe_one_debit / all_pipes_debit * 100
pipe_two_performance = pipe_two_debit / all_pipes_debit * 100

# %%
water_to_pool = all_pipes_debit * hours_missing

# %%
if pool_volume >= water_to_pool:
    water_percentage = water_to_pool / pool_volume * 100
    print(f'The pool is {water_percentage:.2f}% full. Pipe 1: {pipe_one_performance:.2f}%. '
          f'Pipe 2: {pipe_two_performance:.2f}%.')
else:
    water_outside_pool = water_to_pool - pool_volume
    print(f'For {hours_missing:.2f} hours the pool overflows with {water_outside_pool} liters."')
