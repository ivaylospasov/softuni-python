word = ''
printed_word = ''

c_counter = 0
o_counter = 0
n_counter = 0

add_symbol = input()

while add_symbol != 'End':

    if add_symbol.isalpha():
        if add_symbol == 'c' and c_counter == 0:
            c_counter += 1
        elif add_symbol == 'o' and o_counter == 0:
            o_counter += 1
        elif add_symbol == 'n' and n_counter == 0:
            n_counter += 1
        else:
            word += add_symbol

        if c_counter == 1 and o_counter == 1 and n_counter == 1:
            word += ' '
            printed_word = word
            c_counter = 0
            o_counter = 0
            n_counter = 0

    add_symbol = input()

print(printed_word)