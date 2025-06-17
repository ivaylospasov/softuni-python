number_one = int(input())
number_two = int(input())
number_three = int(input())

def smallest_number(first_number, second_number, third_number):
    return min(first_number, second_number, third_number)

print(smallest_number(number_one, number_two, number_three))