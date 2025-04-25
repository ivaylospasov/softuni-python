# Четене на входните шестцифрени числа
first_number = int(input())
second_number = int(input())

# Проверка дали числата са шестцифрени
if 100000 <= first_number <= 999999 and 100000 <= second_number <= 999999 and first_number < second_number:
    # Списък за всички числа, които отговарят на условието
    result_numbers = []

    # Итерация през числата между first_number и second_number (без крайните точки)
    for number in range(first_number + 1, second_number):
        # Преобразуване на числото в стринг за достъп до отделните цифри
        number_string = str(number)

        # Изчисляване на сумите на четните и нечетните позиции
        sum_even_positions = 0  # Позиции 0, 2, 4 (индекси в Python)
        sum_odd_positions = 0   # Позиции 1, 3, 5 (индекси в Python)

        for index in range(len(number_string)):
            digit = int(number_string[index])
            if index % 2 == 0:  # Четна позиция (0, 2, 4)
                sum_even_positions += digit
            else:  # Нечетна позиция (1, 3, 5)
                sum_odd_positions += digit

        # Проверка дали сумите са равни
        if sum_even_positions == sum_odd_positions:
            result_numbers.append(number)

    # Принтиране на резултатите
    if result_numbers:
        print(" ".join(map(str, result_numbers)))
