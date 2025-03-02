# %%
from math import ceil, floor

# %%
grapes_area = int(input())
grapes_per_square_meter = float(input())
wine_volume_needed = int(input())
workers = int(input())

# %%
grapes_for_wine = 0.4 * grapes_area * grapes_per_square_meter
wine_volume_produced = grapes_for_wine / 2.5

# %%
if wine_volume_produced < wine_volume_needed:
    wine_volume_missing = floor(wine_volume_needed - wine_volume_produced)
    print(f'It will be a tough winter! More {wine_volume_missing} liters wine needed.')
else:
    wine_volume_left = wine_volume_produced - wine_volume_needed
    wine_per_worker = ceil(wine_volume_left / workers)
    print(f'Good harvest this year! Total wine: {ceil(wine_volume_produced)} liters.')
    print(f'{ceil(wine_volume_left)} liters left -> {wine_per_worker} liters per person.')
