pages_to_read = int(input())
pages_per_hour = int(input())
days_to_finish = int(input())

total_reading_hours = pages_to_read / pages_per_hour
hours_reading_per_day = int(total_reading_hours / days_to_finish)

print(hours_reading_per_day)
