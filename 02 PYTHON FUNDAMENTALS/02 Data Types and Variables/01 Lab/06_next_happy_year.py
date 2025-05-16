current_year = int(input())
year_set = set()

while True:
    current_year += 1
    year_as_string = str(current_year)
    for letter in year_as_string:
        year_set.add(letter)
    if len(year_set) == len(year_as_string):
        print(year_as_string)
        break
    year_set.clear()