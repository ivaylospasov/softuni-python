word = ''

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
        
        if (add_symbol == 'c' or 
              add_symbol == 'o' or 
              add_symbol == 'n') and (c_counter == 1 and 
                                      o_counter == 1 and 
                                      n_counter == 1):
            word += ' '
            c_counter = 0
            o_counter = 0
            n_counter = 0
        else:
            word += add_symbol

    add_symbol = input()

print(word)