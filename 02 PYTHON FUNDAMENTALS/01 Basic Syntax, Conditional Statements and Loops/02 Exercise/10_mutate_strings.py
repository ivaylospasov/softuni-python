string_one = input()
string_two = input()

for i in range(len(string_one)):
    if string_one[i] != string_two[i]:
        print(f"{string_two[:i]}{string_two[i]}{string_one[i+1:]}")


# Взимаме първата буква от втория низ,
# след това втората буква от втория низ,
# след това остатъка от първия низ.

#  Взимаме първите 2 букви от втория низ,
# след това вторите третата буква от втория низ,
# след това остатъка от първия низ.