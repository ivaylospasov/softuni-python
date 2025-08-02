import re

sentence = input()
searched_word = input()
pattern = fr"\b{searched_word}\b"

matches = re.findall(pattern, sentence, re.IGNORECASE)
#Instead re.IGNORECASE we are using (?i) before the first boundary
# pattern = fr"(?i)\b{searched_word}\b"

print(len(matches))