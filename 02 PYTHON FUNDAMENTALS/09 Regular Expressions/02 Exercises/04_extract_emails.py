import re

text = input()

# Find all variable names that start with underscore followed by letters and digits
pattern = r'\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'

# matches is a list of tuples for all the groups in the pattern
matches = re.findall(pattern, text, re.IGNORECASE)

# Print only the first group in every tuple, because it's the external one
for group in matches:
    print(group[0])