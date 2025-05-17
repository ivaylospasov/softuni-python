key = int(input())
number_of_lines = int(input())

for letter in range(number_of_lines):
    letter_ascii_code = ord(input())
    new_letter = chr(letter_ascii_code + key)
    print(new_letter, end='')

# Alternative shorter but less readable solution
# for _ in range(number_of_lines):
#     letter = input()
#     print(chr(ord(letter) + key), end='')