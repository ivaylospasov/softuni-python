from math import floor

BUILD_TIME = 3
WORKDAY_HOURS = 8
PROCESSOR_PRICE = 110.10

build_target = int(input())
workers_count = int(input())
workdays_count = int(input())

total_working_hours = workers_count * WORKDAY_HOURS * workdays_count
processors_build = floor(total_working_hours / BUILD_TIME)

processors_cost = processors_build * 3.75


money_diff = abs((build_target - processors_build) * PROCESSOR_PRICE)

if build_target <= processors_build:
    print(f'Profit: -> {money_diff:.2f} BGN')
else:
    print(f'Losses: -> {money_diff:.2f} BGN')