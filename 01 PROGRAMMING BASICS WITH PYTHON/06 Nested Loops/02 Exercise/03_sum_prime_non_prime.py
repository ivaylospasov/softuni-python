def is_prime(number):
    """Function that checks if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


sum_prime = 0
sum_non_prime = 0

while True:
    command = input()

    if command.lower() == "stop":
        break

    try:
        number = int(command)
    except ValueError:
        continue

    if number < 0:
        print("Number is negative.")
        continue

    if is_prime(number):
        sum_prime += number
    else:
        sum_non_prime += number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")