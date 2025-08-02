import re

line = input()

# Find all variable names that start with underscore followed by letters and digits
pattern = r'(w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+)'

while line:
    match = re.search(pattern, line)

    if match:
        link = match.group(1)
        print(link)

    line = input()