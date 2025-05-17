n = int(input())
word = input()

list_of_words = []
filtered_words_list = []

for i in range(n):
    current_word = input()
    list_of_words.append(current_word)
    if word in current_word:
        filtered_words_list.append(current_word)

print(list_of_words)
print(filtered_words_list)

