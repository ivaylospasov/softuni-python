from math import floor

open_tabs = int(input())
salary = float(input())

for i in range(1, open_tabs + 1):
    website = input().lower()
    if website == 'facebook':
        salary -= 150
        if salary <= 0:
            print('You have lost your salary.')
            break
    elif website == 'instagram':
        salary -= 100
        if salary <= 0:
            print('You have lost your salary.')
            break
    elif website == 'reddit':
        salary -= 50
        if salary <= 0:
            print('You have lost your salary.')
            break

if salary > 0:
    print(f'{floor(salary)}')