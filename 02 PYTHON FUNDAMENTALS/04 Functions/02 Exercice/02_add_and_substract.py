first_number = int(input())
second_number = int(input())
third_number = int(input())

def sum_numbers(x, y):
    return x + y

def subtract(a, b, c):
    return sum_numbers(a, b) - c

def add_and_subtract(number_one, number_two, number_three):
    print(subtract(number_one, number_two, number_three))

add_and_subtract(first_number, second_number, third_number)