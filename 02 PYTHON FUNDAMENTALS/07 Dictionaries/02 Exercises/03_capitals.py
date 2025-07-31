countries = input().split(", ")
capitals = input().split(", ")

# Direct solution, no dictionaries
# for country, capital in zip(countries, capitals):
#     print(f"{country} -> {capital}")

country_capitals = {country: capital for country, capital in zip(countries, capitals)}
# ИЛИ
# country_capitals = {countries[index]:capitals[index] for index in range(len(countries))}

for country, capital in country_capitals.items():
    print(f"{country} -> {capital}")