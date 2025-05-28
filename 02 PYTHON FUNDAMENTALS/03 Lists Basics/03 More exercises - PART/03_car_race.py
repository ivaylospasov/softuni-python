car_steps = input().split(' ')
car_steps_as_int = [int(x) for x in car_steps]

car_steps_count = len(car_steps_as_int) // 2

first_car_steps = car_steps_as_int[:car_steps_count]
second_car_steps = car_steps_as_int[:car_steps_count:-1]

first_car_total_time = 0
second_car_total_time = 0

for i in first_car_steps:
    if i == 0:
        first_car_total_time *= 0.8
    else:
        first_car_total_time += i

for i in second_car_steps:
    if i == 0:
        second_car_total_time *= 0.8
    else:
        second_car_total_time += i

if first_car_total_time < second_car_total_time:
    print(f"The winner is left with total time: {first_car_total_time:.1f}")
elif second_car_total_time < first_car_total_time:
    print(f"The winner is right with total time: {second_car_total_time:.1f}")
else:
    pass