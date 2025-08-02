import re

numbers = []
line = input()

while line:
    # Find all numbers in the current line
    matches = re.findall(r'\d+', line)
    numbers.extend(matches)

    line = input()

# Print all numbers on a single line separated by space
print(' '.join(numbers))