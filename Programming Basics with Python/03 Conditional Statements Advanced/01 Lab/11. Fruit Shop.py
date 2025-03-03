fruit = input()
day_of_week = input()
quantity = float(input())

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
fruits = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
holidays = ['Saturday', 'Sunday']
price = 0

if day_of_week in weekdays and fruit in fruits:
    if day_of_week in workdays:
        if fruit == 'banana':
            price = 2.5
        elif fruit == 'apple':
            price = 1.2
        elif fruit == 'orange':
            price = 0.85
        elif fruit == 'grapefruit':
            price = 1.45
        elif fruit == 'kiwi':
            price = 2.7
        elif fruit == 'pineapple':
            price = 5.5
        elif fruit == 'grapes':
            price = 3.85
        total_cost = price * quantity
        print(f'{total_cost:.2f}')
    elif day_of_week in holidays:
        if fruit == 'banana':
            price = 2.7
        elif fruit == 'apple':
            price = 1.25
        elif fruit == 'orange':
            price = 0.9
        elif fruit == 'grapefruit':
            price = 1.6
        elif fruit == 'kiwi':
            price = 3
        elif fruit == 'pineapple':
            price = 5.6
        elif fruit == 'grapes':
            price = 4.2
        total_cost = price * quantity
        print(f'{total_cost:.2f}')
else:
    print('error')

