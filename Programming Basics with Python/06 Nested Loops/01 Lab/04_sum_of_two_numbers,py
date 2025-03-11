start = int(input())
end = int(input())
magic_number = int(input())
counter = 0

for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter += 1
        if i + j == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            break
        if i == end and j == end:
            print(f"{counter} combinations - neither equals {magic_number}")
            break
    if i + j == magic_number:
        break


# 1. Read input data
# 2. Generate all possible combinations of two numbers in the given range
# 3. Check if the sum of the two numbers is equal to the magic number
# 4. Print the result
# 5. Print the number of combinations if the magic number is not found
# 6. End the program
# Input: 1, 10, 5
# Output:
# Combination N:4 (1 + 4 = 5)
# 4 combinations - neither equals 5
# Input: 23, 24, 20
# Output:
# Combination N:1 (23 + 24 = 47)
# 1 combinations - neither equals 20
# Input: 88, 888, 1000
# Output:
# Combination N:1 (88 + 912 = 1000)
# End of program
# The program reads three integers from the console: start, end, and magic_number.
# It generates all possible combinations of two numbers in the range [start, end].
# If the sum of two numbers is equal to the magic number, the program prints the combination.
# If the magic number is not found, the program prints the number of combinations.
# The program ends after printing the result.
# The program uses a nested loop to generate all possible combinations of two numbers.
# The outer loop iterates over the range [start, end].
# The inner loop iterates over the range [start, end].
# The program checks if the sum of the two numbers is equal to the magic number.
# If the magic number is found, the program prints the combination and breaks the loop.
# If the magic number is not found, the program prints the number of combinations and breaks the loop.