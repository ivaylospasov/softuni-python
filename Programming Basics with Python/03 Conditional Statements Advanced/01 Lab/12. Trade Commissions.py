city = input().lower()
sales = float(input())

if (city == 'sofia' or
    city == 'varna' or
    city == 'plovdiv') and sales >= 0:
    if city == 'sofia':
        if 0 <= sales <= 500:
            commission = 0.05
        elif 500 <= sales <= 1000:
            commission = 0.07
        elif 1000 <= sales <= 10000:
            commission = 0.08
        elif 10000 < sales:
            commission = 0.12
    elif city == 'varna':
        if 0 <= sales <= 500:
            commission = 0.045
        elif 500 <= sales <= 1000:
            commission = 0.075
        elif 1000 <= sales <= 10000:
            commission = 0.10
        elif 10000 < sales:
            commission = 0.13
    elif city == 'plovdiv':
        if 0 <= sales <= 500:
            commission = 0.055
        elif 500 <= sales <= 1000:
            commission = 0.08
        elif 1000 <= sales <= 10000:
            commission = 0.12
        elif 10000 < sales:
            commission = 0.145
    bonus = commission * sales
    print(f'{bonus:.2f}')
else:
    print('error')

