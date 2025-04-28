cargo_count = int(input())

cargo_weight = 0
total_cargo_weight = 0
total_tons_by_bus = 0
total_tons_by_truck = 0
total_tons_by_train = 0
total_cargo_price = 0

for cargo in range(1, cargo_count + 1):
    cargo_weight = int(input())
    if cargo_weight <= 3:
        total_tons_by_bus += cargo_weight
        total_cargo_price += (200 * cargo_weight)
        total_cargo_weight += cargo_weight
    elif 4 <= cargo_weight <= 11:
        total_tons_by_truck += cargo_weight
        total_cargo_price += (175 * cargo_weight)
        total_cargo_weight += cargo_weight
    elif 12 <= cargo_weight:
        total_tons_by_train += cargo_weight
        total_cargo_price += (120 * cargo_weight)
        total_cargo_weight += cargo_weight

average_cargo_ton_price = total_cargo_price / total_cargo_weight
percent_tons_by_bus = total_tons_by_bus / total_cargo_weight * 100
percent_truck_cargos = total_tons_by_truck / total_cargo_weight * 100
percent_train_cargos = total_tons_by_train / total_cargo_weight * 100

print(f'{average_cargo_ton_price:.2f}')
print(f'{percent_tons_by_bus:.2f}%')
print(f'{percent_truck_cargos:.2f}%')
print(f'{percent_train_cargos:.2f}%')