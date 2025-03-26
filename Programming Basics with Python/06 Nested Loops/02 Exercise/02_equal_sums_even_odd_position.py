#TODO Защо на някои тестове се получава грешен отговор? Защо в упътването искат в range второто число да е +1?

# Четене на входните числа
number_one = int(input())
number_two = int(input())

# Списък за всички числа, които отговарят на условието
result_numbers = []

# Итерация през числата между number_one и number_two
for number in range(number_one + 1, number_two):
    sum_odd_positions = 0
    sum_even_positions = 0

    # Преобразуване на числото в стринг за достъп до отделните цифри
    number_string = str(number)

    # Изчисляване на сумите на четните и нечетните позиции
    for index in range(len(number_string)):
        digit = int(number_string[index])
        if (index + 1) % 2 != 0:  # Нечетна позиция
            sum_odd_positions += digit
        else:  # Четна позиция
            sum_even_positions += digit

    # Проверка дали сумите са равни
    if sum_odd_positions == sum_even_positions:
        result_numbers.append(number)

# Принтиране на резултатите
if result_numbers:
    print(" ".join(map(str, result_numbers)))