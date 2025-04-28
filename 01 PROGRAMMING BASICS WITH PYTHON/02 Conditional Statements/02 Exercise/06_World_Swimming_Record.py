record_time = float(input())
swimming_distance = float(input())
time_by_meter = float(input())

standard_time = swimming_distance * time_by_meter
time_delay = swimming_distance // 15 * 12.5
total_time = standard_time + time_delay

if total_time < record_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    time_slower = total_time - record_time
    print(f'No, he failed! He was {time_slower:.2f} seconds slower.')
