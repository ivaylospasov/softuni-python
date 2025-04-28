# my_text = input()
#
# vowels_sum = 0
#
# for char in my_text:
#     if char == 'a':
#         vowels_sum += 1
#     elif char == 'e':
#         vowels_sum += 2
#     elif char == 'i':
#         vowels_sum += 3
#     elif char == 'o':
#         vowels_sum += 4
#     elif char == 'u':
#         vowels_sum += 5
#
# print(vowels_sum)

# Решение от презентацията

my_text = input()
vowels_sum = 0

for i in range(0, len(my_text)):
    if my_text[i] in 'a':
        vowels_sum += 1
    elif my_text[i] in 'e':
        vowels_sum += 2
    elif my_text[i] in 'i':
        vowels_sum += 3
    elif my_text[i] in 'o':
        vowels_sum += 4
    elif my_text[i] in 'u':
        vowels_sum += 5

print(vowels_sum)