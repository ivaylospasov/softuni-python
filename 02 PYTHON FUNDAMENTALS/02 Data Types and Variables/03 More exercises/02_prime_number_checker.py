from math import sqrt

n = int(input())

if n <= 1:
    print(False)
else:
    is_prime = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)

# Check if n <= 1, if true, it's not prime.
# Loop from 2 to the square root of n, if n % i == 0, it's not prime. If no divisors found, n is prime.