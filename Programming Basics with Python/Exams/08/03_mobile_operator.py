ONE_SMALL = 9.98 # one year contract - small type
ONE_MIDDLE = 18.99 # one year contract - middle type
ONE_LARGE = 25.98 # one year contract - large type
ONE_EXTRA_LARGE = 35.99 # one year contract - extra large type

TWO_SMALL = 8.58
TWO_MIDDLE = 17.09
TWO_LARGE = 23.59
TWO_EXTRA_LARGE = 31.79

INTERNET_LESS_OR_EQUAL_TO_10 = 5.5
INTERNET_LESS_OR_EQUAL_TO_30 = 4.35
INTERNET_MORE_THAN_30 = 3.85

TWO_YEAR_CONTRACT_DISCOUNT = 0.0375

contract_duration = input().lower() # one or two
contract_type = input().lower() # small, middle, lange, extralarge
internet_included = input().lower() # yes, no
number_of_months = int(input()) # 1 to 24

if contract_duration == 'one':
    if contract_type == 'small':
        if internet_included == 'yes':
            total_price = number_of_months * (ONE_SMALL + INTERNET_LESS_OR_EQUAL_TO_10)
        else:
            total_price = number_of_months * ONE_SMALL
    elif contract_type == 'middle':
        if internet_included == 'yes':
            total_price = number_of_months * (ONE_MIDDLE + INTERNET_LESS_OR_EQUAL_TO_30)
        else:
            total_price = number_of_months * ONE_MIDDLE
    elif contract_type == 'large':
        if internet_included == 'yes':
            total_price = number_of_months * (ONE_LARGE + INTERNET_LESS_OR_EQUAL_TO_30)
        else:
            total_price = number_of_months * ONE_LARGE
    else:
        if internet_included == 'yes':
            total_price = number_of_months * (ONE_EXTRA_LARGE + INTERNET_MORE_THAN_30)
        else:
            total_price = number_of_months * ONE_EXTRA_LARGE
elif contract_duration == 'two':
    if contract_type == 'small':
        if internet_included == 'yes':
            total_price = number_of_months * (TWO_SMALL + INTERNET_LESS_OR_EQUAL_TO_10) * (1 - TWO_YEAR_CONTRACT_DISCOUNT)
        else:
            total_price = number_of_months * TWO_SMALL * (1 - TWO_YEAR_CONTRACT_DISCOUNT)
    elif contract_type == 'middle':
        if internet_included == 'yes':
            total_price = number_of_months * (TWO_MIDDLE + INTERNET_LESS_OR_EQUAL_TO_30) * (1 - TWO_YEAR_CONTRACT_DISCOUNT)
        else:
            total_price = number_of_months * TWO_MIDDLE * (1 - TWO_YEAR_CONTRACT_DISCOUNT)
    elif contract_type == 'large':
        if internet_included == 'yes':
            total_price = number_of_months * (TWO_LARGE + INTERNET_LESS_OR_EQUAL_TO_30) * (1 - TWO_YEAR_CONTRACT_DISCOUNT)
        else:
            total_price = number_of_months * TWO_LARGE * (1 - TWO_YEAR_CONTRACT_DISCOUNT)
    else:
        if internet_included == 'yes':
            total_price = number_of_months * (TWO_EXTRA_LARGE + INTERNET_MORE_THAN_30) * (1 - TWO_YEAR_CONTRACT_DISCOUNT)
        else:
            total_price = number_of_months * TWO_EXTRA_LARGE * (1 - TWO_YEAR_CONTRACT_DISCOUNT)

print(f'{total_price:.2f} lv.')