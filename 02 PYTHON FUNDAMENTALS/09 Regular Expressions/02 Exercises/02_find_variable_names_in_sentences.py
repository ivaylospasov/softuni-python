import re

text = input()

# Find all variable names that start with underscore followed by letters and digits
pattern = r'\b_([A-Za-z0-9]+)\b'
matches = re.findall(pattern, text)

# Print all variable names on a single line, separated by commas
print(','.join(matches))