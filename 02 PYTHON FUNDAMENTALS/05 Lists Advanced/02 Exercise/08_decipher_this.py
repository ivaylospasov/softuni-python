words = input().split()

deciphered_message = []

for word in words:
    word = [char for char in word]
    number_as_string = ""

    for index in range(len(word)):
        if word[index].isdigit():
            number_as_string += word[index]
        else:
            break

    digits_as_letter = chr(int(number_as_string))
    word_letters = word[index:]
    word_letters[0], word_letters[-1] = word_letters[-1], word_letters[0]
    deciphered_word = digits_as_letter + "".join(word_letters)
    deciphered_message.append(deciphered_word)

print(" ".join(deciphered_message))