char_count = int(input())
char_sum = 0

for _ in range(char_count):
    char_sum += ord(input())

print(f'The sum equals: {char_sum}')