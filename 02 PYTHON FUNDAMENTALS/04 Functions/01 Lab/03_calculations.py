operator = input()
first_number = int(input())
second_number = int(input())

def calculator(given_operator: str, number_one: float, number_two: float):
    """
    This is a calculator function.
    :param given_operator:
    :param number_one:
    :param number_two:
    :return:
    """
    result = None
    if given_operator == 'multiply':
        result = number_one * number_two
    elif given_operator == 'divide':
        if number_two != 0:
            result = int(number_one / number_two)
        else:
            pass
    elif given_operator == 'add':
        result = number_one + number_two
    elif given_operator == 'subtract':
        result = number_one - number_two
    return result

print(calculator(operator, first_number, second_number))