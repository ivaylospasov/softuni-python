import io
import sys
from contextlib import redirect_stdout
from zoo import Zoo

# Test case from the example
test_input = """Great Zoo
5
mammal lion
mammal bear
fish salmon
bird owl
mammal tiger
mammal"""

# Expected output
expected_output = """Mammals in Great Zoo: lion, bear, tiger
Total animals: 5"""

# Redirect stdin to use our test input
sys.stdin = io.StringIO(test_input)

# Capture stdout
f = io.StringIO()
with redirect_stdout(f):
    # Run the main program logic
    zoo_name = input()
    zoo = Zoo(zoo_name)

    n = int(input())

    for _ in range(n):
        animal_info = input().split()
        species = animal_info[0]
        name = animal_info[1]
        zoo.add_animal(species, name)

    species = input()
    print(zoo.get_info(species))

# Get the output
output = f.getvalue().strip()

# Compare with expected output
print("Test passed:", output == expected_output)
print("\nActual output:")
print(output)
print("\nExpected output:")
print(expected_output)